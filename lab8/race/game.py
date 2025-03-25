import pygame
import random
import os
import math

# Game Settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SPEED = 3  # Movement speed of entities
FPS = 60   # Frames per second

#Initialize Pygame
pygame.init()
pygame.font.init()

#Base Class for Entities
class Entity:
    def __init__(self, width, aspect_ratio, image_path, speed):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.height = self.width / self.aspect_ratio

        # Load and scale image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, int(self.height)))
        self.rect = self.image.get_rect()
        self.MOVEMENT_SPEED = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

#Player Class
class Player(Entity):
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "images", "cars", "car_purple.png")
        super().__init__(60, 0.5, path, SPEED * 4)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.MOVEMENT_SPEED, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.MOVEMENT_SPEED, 0)

#Base Class for Obstacles
class Obstacle(Entity):
    def __init__(self, width, aspect_ratio, image_path, speed):
        super().__init__(width, aspect_ratio, image_path, speed)
        self.rect.center = self.randomize_position()

    def randomize_position(self):
        y = int(-self.height)
        x = random.randint(10, SCREEN_WIDTH - 10 - self.rect.width)
        return x, y

    def move(self):
        self.rect.move_ip(0, self.MOVEMENT_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.__init__()

# Enemy Car Class 
class Enemy(Obstacle):
    def __init__(self):
        cars_path = os.path.join(os.path.dirname(__file__), "images", "cars")
        cars = os.listdir(cars_path)
        super().__init__(60, 0.5, os.path.join(cars_path, random.choice(cars)), SPEED)
        self.image = pygame.transform.rotate(self.image, 180)  # Flip car image

#Coin Class
class Coin(Obstacle):
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "images", "coin.png")
        super().__init__(20, 1, path, SPEED)

#Main Game Class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Racing Game")
        self.running = True
        self.font = pygame.font.SysFont("Courier New", 40)

        self.create_bg()
        self.create_entities()
        self.create_counters()

    def create_bg(self):
        path = os.path.join(os.path.dirname(__file__), "images", "bg.png")
        self.bg = pygame.image.load(path)
        bg_aspect_ratio = self.bg.get_width() / self.bg.get_height()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, math.ceil(SCREEN_WIDTH / bg_aspect_ratio)))
        self.copies = math.ceil(SCREEN_HEIGHT / self.bg.get_height()) + 1

    def draw_bg(self):
        self.screen.fill(WHITE)
        self.scroll = (self.scroll + self.speed // 1.5) % self.bg.get_height()
        for i in range(self.copies):
            self.screen.blit(self.bg, (0, self.scroll + (i - 1) * (self.bg.get_height() - 1)))

    def create_counters(self):
        self.scroll = 0
        self.coins = 0
        self.speed = SPEED

    def draw_coin_counter(self):
        coins_counter = self.font.render(str(self.coins), True, BLACK)
        pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH - 60, 0, 60, 60))
        self.screen.blit(coins_counter, (SCREEN_WIDTH - 50, 10))

    def create_entities(self):
        self.player = Player()
        self.enemy = Enemy()
        self.coin = Coin()

    def draw_entities(self):
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.coin.draw(self.screen)
        self.player.move()
        self.enemy.move()
        self.coin.move()

    def watch_collisions(self):
        if self.player.rect.colliderect(self.enemy.rect):
            self.screen.fill(RED)  # Flash red when colliding with enemy
            self.running = False   # End game

        if self.player.rect.colliderect(self.coin.rect):
            self.coin.__init__()  # Respawn coin
            self.coins += 1       # Increase score

        if self.enemy.rect.colliderect(self.coin.rect):
            self.coin.__init__()  # Respawn coin if an enemy touches it

    def watch_events(self):
        #Handle user inputs and exit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        #Main game loop
        clock = pygame.time.Clock()
        while self.running:
            self.watch_events()
            self.watch_collisions()
            self.draw_bg()
            self.draw_entities()
            self.draw_coin_counter()
            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()