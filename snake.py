import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

# Window setup
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("The snake never sleeps")
time.sleep(2)

# Game constants
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("constantia", 30)

def user_score(score):
    value = score_font.render("Score: " + str(score), True, green)
    window.blit(value, [10, 10])

def game_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, red, [x[0], x[1], snake_block, snake_block])

def message_center(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(win_width // 2, win_height // 2))
    window.blit(mesg, mesg_rect)

def game_loop():
    x1 = win_width / 2
    y1 = win_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            window.fill(grey)
            message_center("You lost! Press P to Play Again or Q to Quit", red)
            user_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        return  # Return to main loop to restart

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        game_snake(snake_block, snake_list)
        user_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def main():
    while True:
        game_loop()

main()
