# Gravity
import pygame
import time

pygame.init()
display_height = 800
display_width = 1000
screen = pygame.display.set_mode((display_height, display_width))
white = 255, 255, 255
PlayerImg = pygame.draw.rect(screen, white, (50, 50, 20, 500))


def Character(x, y):
        screen.blit(PlayerImg, (x, y))


def main():

    while True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            if event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_w:
                ychange = -5
            if event.key == pygame.K_s:
                ychange = 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


main()
