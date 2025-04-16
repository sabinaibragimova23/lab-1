import pygame
import random
import time
import psycopg2
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.font.init()

# Database connection
def create_connection():
    return psycopg2.connect(
        database="snake", 
        user="postgres", 
        password="87779626062", 
        host="localhost", 
        port="5432")

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "User" (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES "User"(user_id),
        level INT NOT NULL,
        score INT NOT NULL,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()

def get_user_id(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM \"User\" WHERE username = %s", (username,))
    result = cur.fetchone()
    
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO \"User\" (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def get_last_score(conn, user_id):
    cur = conn.cursor()
    cur.execute("""
        SELECT level, score FROM user_score 
        WHERE user_id = %s 
        ORDER BY saved_at DESC 
        LIMIT 1
    """, (user_id,))
    return cur.fetchone()

def save_score(conn, user_id, level, score):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO user_score (user_id, level, score)
        VALUES (%s, %s, %s)
    """, (user_id, level, score))
    conn.commit()

# Game settings
WIDTH, HEIGHT = 600, 400
GRID = 25
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Walls for different levels
def create_walls(level):
    walls = []
    # Border walls for all levels
    for x in range(0, WIDTH, GRID):
        walls.append(pygame.Rect(x, 0, GRID, GRID))
        walls.append(pygame.Rect(x, HEIGHT-GRID, GRID, GRID))
    for y in range(0, HEIGHT, GRID):
        walls.append(pygame.Rect(0, y, GRID, GRID))
        walls.append(pygame.Rect(WIDTH-GRID, y, GRID, GRID))
    
    # Level 2 walls
    if level >= 2:
        for x in range(5*GRID, 10*GRID, GRID):
            walls.append(pygame.Rect(x, 10*GRID, GRID, GRID))
    
    # Level 3 walls
    if level >= 3:
        for y in range(5*GRID, 15*GRID, GRID):
            walls.append(pygame.Rect(15*GRID, y, GRID, GRID))
    
    return walls

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = RED
        self.points = 1
        self.spawn_time = 0
        self.life = 0
    
    def new(self, snake=None, walls=None):
        while True:
            self.x = random.randint(1, (WIDTH//GRID)-2)*GRID
            self.y = random.randint(1, (HEIGHT//GRID)-2)*GRID
            if (not snake or (self.x, self.y) not in snake) and \
               (not walls or not any(wall.collidepoint(self.x, self.y) for wall in walls)):
                break
        
        if random.random() < 0.2:
            self.color = BLUE
            self.points = 3
            self.life = 5
        else:
            self.color = RED
            self.points = 1
            self.life = 0
        
        self.spawn_time = time.time()
    
    def check_time(self):
        if self.life > 0 and (time.time()-self.spawn_time) > self.life:
            return True
        return False

def show_message(surface, msg, color, size=48, y_offset=0):
    font = pygame.font.Font(None, size)
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    surface.blit(text, text_rect)

def pause_game(conn, user_id, level, score):
    save_score(conn, user_id, level, score)
    paused = True
    
    while paused:
        screen.fill(BLACK)
        show_message(screen, "PAUSED", YELLOW)
        show_message(screen, "Press P to continue", WHITE, 24, 50)
        show_message(screen, "Press Q to quit", WHITE, 24, 80)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    paused = False
                elif event.key == K_q:
                    return False
    
    return True

def show_welcome_screen(username, last_level, last_score):
    screen.fill(BLACK)
    show_message(screen, f"Welcome, {username}!", GREEN)
    
    if last_level:
        show_message(screen, f"Last level: {last_level}", WHITE, 24, 50)
        show_message(screen, f"Last score: {last_score}", WHITE, 24, 80)
    else:
        show_message(screen, "New player! Starting from level 1", WHITE, 24, 50)
    
    show_message(screen, "Press any key to start", WHITE, 24, 120)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN:
                waiting = False
    return True

# Main Game Loop
def game_loop(conn, username):
    user_id = get_user_id(conn, username)
    last_score = get_last_score(conn, user_id)
    
    if last_score:
        last_level, last_score = last_score
    else:
        last_level, last_score = None, None
    
    if not show_welcome_screen(username, last_level, last_score):
        return
    
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = (GRID, 0)
    score = 0
    level = 1
    speed = 5
    game_over = False
    walls = create_walls(level)
    
    food = Food()
    food.new(snake, walls)

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != (0, GRID):
                    direction = (0, -GRID)
                elif event.key == K_DOWN and direction != (0, -GRID):
                    direction = (0, GRID)
                elif event.key == K_LEFT and direction != (GRID, 0):
                    direction = (-GRID, 0)
                elif event.key == K_RIGHT and direction != (-GRID, 0):
                    direction = (GRID, 0)
                elif event.key == K_p:
                    if not pause_game(conn, user_id, level, score):
                        game_over = True
        
        if game_over:
            break
        
        new_x = snake[0][0] + direction[0]
        new_y = snake[0][1] + direction[1]
        new_head = (new_x, new_y)
        
        # Check collisions
        if (new_x < 0 or new_x >= WIDTH or 
            new_y < 0 or new_y >= HEIGHT or 
            new_head in snake or
            any(wall.collidepoint(new_x, new_y) for wall in walls)):
            game_over = True
            save_score(conn, user_id, level, score)
            break
        
        snake.insert(0, new_head)
        
        # Check food
        if new_head == (food.x, food.y):
            score += food.points
            if score % 5 == 0:  # Level up every 5 points
                level += 1
                speed += 2
                walls = create_walls(level)
            food.new(snake, walls)
        else:
            snake.pop()
        
        # Check food expiration
        if food.check_time():
            food.new(snake, walls)
        
        # Drawing
        screen.fill(BLACK)
        
        # Draw walls
        for wall in walls:
            pygame.draw.rect(screen, GRAY, wall)
        
        # Draw food
        pygame.draw.rect(screen, food.color, (food.x, food.y, GRID, GRID))
        
        # Draw snake
        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], GRID, GRID))
        
        # Draw score
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(speed)
    
    # Game over screen
    while game_over:
        screen.fill(BLACK)
        show_message(screen, "GAME OVER", RED)
        show_message(screen, f"Final Score: {score}", WHITE, 24, 50)
        show_message(screen, f"Level: {level}", WHITE, 24, 80)
        show_message(screen, "Press R to restart", WHITE, 24, 120)
        show_message(screen, "Press Q to quit", WHITE, 24, 150)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    return True
                elif event.key == K_q:
                    return False

def main():
    conn = create_connection()
    create_tables(conn)
    
    username = input("Enter your username: ")
    
    restart = True
    while restart:
        restart = game_loop(conn, username)
    
    conn.close()
    pygame.quit()

if __name__ == "__main__":
    main()