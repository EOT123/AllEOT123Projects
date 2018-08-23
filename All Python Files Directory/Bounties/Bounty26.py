# Mouse Watcher: Tracks Mouse
import pygame

pygame.init()


white = 255, 255, 255
display_width = 700
display_height = 600
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(white)
    pygame.display.update()
    clock.tick(60)
