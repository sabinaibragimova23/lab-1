import pygame
import time
import random

# Initial snake speed
snake_speed = 10

# Window size
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Create game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (Frames Per Second) controller
fps = pygame.time.Clock()

# Default snake position
snake_position = [100, 50]

# Define the initial snake body (4 blocks)
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Function to generate fruit that does not overlap with the snake
def generate_fruit():
    while True:
        new_fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        if new_fruit_position not in snake_body:
            return new_fruit_position

# Initial fruit position
fruit_position = generate_fruit()
fruit_spawn = True

# Default snake movement direction
direction = 'RIGHT'
change_to = direction

# Initial score and level
score = 0
level = 1

# Function to display the score and level
def show_score_and_level():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}  Level: {level}', True, white)
    game_window.blit(score_surface, (10, 10))

# Function to handle game over
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Your Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x // 2, window_y // 4))
    
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Wait for 2 seconds before exiting
    time.sleep(2)
    pygame.quit()
    quit()

# Main Game Loop
while True:
    # Handling key events for movement
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update movement direction
    direction = change_to

    # Move the snake in the current direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body mechanics
    snake_body.insert(0, list(snake_position))
    
    # Check if the snake eats the fruit
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False

        # Increase level every 3 fruits (30 points)
        if score % 30 == 0:
            level += 1
            snake_speed += 2  # Increase snake speed

    else:
        snake_body.pop()  # Remove last block if no fruit is eaten

    # Spawn a new fruit if the previous one was eaten
    if not fruit_spawn:
        fruit_position = generate_fruit()
    fruit_spawn = True

    # Clear screen
    game_window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw the fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for wall collisions (game over)
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    # Check for collision with itself (game over)
    if snake_position in snake_body[1:]:
        game_over()

    # Display score and level
    show_score_and_level()

    # Update the game window
    pygame.display.update()

    # Control game speed
    fps.tick(snake_speed)
