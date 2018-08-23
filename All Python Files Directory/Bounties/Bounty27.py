# Lots Of Shapes: Make Various Shapes
import pygame


def main():
    pygame.init()

    display_width = 1000
    display_height = 600
    screen = pygame.display.set_mode((display_width, display_height))

    BLACK = 0, 0, 0
    BLUE = 0, 0, 255
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (400, 300, 450, 50))
    pygame.draw.circle(screen, BLACK, (600, 150), 50)
    pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(screen, BLUE, (60, 300), (120, 300), 4)
    pygame.draw.line(screen, BLUE, (120, 300), (60, 360))
    pygame.draw.line(screen, BLUE, (60, 360), (120, 360), 4)
    pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)
    pygame.draw.ellipse(screen, RED, (300, 200, 40, 80), 1)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


main()
