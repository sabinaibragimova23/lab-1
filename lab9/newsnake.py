import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
CELL = 30
FPS_INITIAL = 5

# Colors
colorGRAY = (100, 100, 100)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)
colorORANGE = (255, 165, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

# Setup display
font = pygame.font.SysFont("Verdana", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image_game_over = font.render("NEW LEVEL! +2 TO SPEED", True, colorBLACK)
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
game_over_text = font.render("GAME OVER! Press R to restart", True, colorRED)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game variables
cnt = 0
level_up_shown = False
level = 0
cnt_weigh = 0
fps = FPS_INITIAL
game_active = True

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        global game_active
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Check wall collision
        if (self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or 
            self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL):
            game_active = False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()
            return True

    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

class Different_Weigh_Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorORANGE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

class DisappearingFood:
    def __init__(self):
        self.pos = Point(9, 9)
        self.visible = True
        self.spawn_time = pygame.time.get_ticks()
        self.appear_interval = 5000  # appears every 5 seconds
        self.visible_duration = 3000  # visible for 3 seconds

    def draw(self):
        current_time = pygame.time.get_ticks()
        if self.visible and current_time - self.spawn_time > self.visible_duration:
            self.visible = False
        elif not self.visible and current_time - self.spawn_time > self.appear_interval:
            self.visible = True
            self.generate_random_pos()
            self.spawn_time = current_time
        if self.visible:
            pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

# Game initialization
clock = pygame.time.Clock()
food = Food()
snake = Snake()
weigh_food = Different_Weigh_Food()
disappear = DisappearingFood()
running = True

def reset_game():
    global snake, food, weigh_food, disappear, cnt, level, fps, game_active, level_up_shown
    snake = Snake()
    food = Food()
    weigh_food = Different_Weigh_Food()
    disappear = DisappearingFood()
    cnt = 0
    level = 0
    fps = FPS_INITIAL
    game_active = True
    level_up_shown = False

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
            else:
                if event.key == pygame.K_r:
                    reset_game()

    screen.fill(colorBLACK)
    draw_grid()

    if game_active:
        snake.move()
        
        # Check self collision
        if snake.check_self_collision():
            game_active = False

        # Collision with regular food
        if snake.check_collision(food):
            cnt += 1
            level_up_shown = False

        # Collision with weighted food
        if snake.check_collision(weigh_food):
            weigh = random.randint(1, 4)
            cnt += weigh

        # Collision with disappearing food
        if disappear.visible and snake.body[0].x == disappear.pos.x and snake.body[0].y == disappear.pos.y:
            cnt += 2
            disappear.visible = False
            disappear.spawn_time = pygame.time.get_ticks()

        # Level up
        if cnt != 0 and cnt % 4 == 0 and not level_up_shown:
            screen.fill(colorRED)
            screen.blit(image_game_over, image_game_over_rect)
            pygame.display.flip()
            time.sleep(1)
            fps += 2
            level_up_shown = True
            level += 1

        # Draw everything
        snake.draw()
        food.draw()
        weigh_food.draw()
        disappear.draw()

        # Display text
        image_counter = font.render(f"counter: {cnt}", True, colorRED)
        image_counter_rect = image_counter.get_rect(center=(450, 20))
        screen.blit(image_counter, image_counter_rect)

        image_new_level = font.render(f"level: {level}", True, colorRED)
        image_new_level_rect = image_new_level.get_rect(center=(300, 20))
        screen.blit(image_new_level, image_new_level_rect)
    else:
        screen.blit(game_over_text, game_over_rect)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()