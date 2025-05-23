import pygame
import random
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Load sounds
pygame.mixer.music.load("corporate-background-music-345199.mp3")
pygame.mixer.music.play(-1)  # Loop background music
eat_sound = pygame.mixer.Sound("eating-sound-effect-36186.mp3")
gameover_sound = pygame.mixer.Sound("341695__aceofspadesproduc100__coins-1.wav")

# Colors (new theme: dark background + neon snake)
background_color = (18, 18, 18)
snake_color = (0, 255, 0)  # Neon Green
food_color = (255, 0, 255)  # Neon Pink
text_color = (200, 200, 200)

# Screen setup
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Enhanced Snake Game')

# Game variables
snake_block = 20
snake_speed = 15
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("consolas", 30)
score_font = pygame.font.SysFont("consolas", 35)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, text_color)
    window.blit(value, [10, 10])

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    rect = mesg.get_rect(center=(width / 2, height / 2 + y_offset))
    window.blit(mesg, rect)

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(background_color)
            message("You Lost! Press Q to Quit or C to Play Again", food_color)
            pygame.display.update()
            pygame.mixer.music.stop()
            gameover_sound.play()
            time.sleep(2)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(background_color)
        pygame.draw.rect(window, food_color, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            eat_sound.play()
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
