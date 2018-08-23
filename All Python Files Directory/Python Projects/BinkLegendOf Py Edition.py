import pygame
import time
import random

pygame.init()

list = [0, 0]

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Bink Legend Of')
clock = pygame.time.Clock()

BinkImg = pygame.image.load('D:/Pictures/link.png')
gameIcon = pygame.image.load('D:/Pictures/link.png')

pygame.display.set_icon(gameIcon)

pause = False


# crash = True

def main_game():
    game_status = GameStatus()
    # ...
    # when player gets hurt
    game_status.reduce_health()
    # ...


def game_over():
    print("game over, sorry")


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def Bink(x, y):
    gameDisplay.blit(BinkImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def paused():
    font = pygame.font.SysFont("comicsansms", 25)
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText, )
    text = font.render("Paused")
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue Your Misery", 150, 300, 200, 50, green, bright_green, unpause)
        button("End Your Life", 500, 300, 200, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 110)
        TextSurf, TextRect = text_objects("Bink Legend Of", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start Your Torture!", 150, 450, 200, 50, green, bright_green, game_loop)
        button("Give Up", 500, 450, 200, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(8)


def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    ychange = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    gameDisplay.fill(black)
                    paused()
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    gameDisplay.fill(black)
                    paused()
                if event.key == pygame.K_w:
                    ychange = -5
                if event.key == pygame.K_s:
                    ychange = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    ychange = 0

        x += x_change
        y += ychange
        gameDisplay.fill(white)

        Bink(x, y)

        pygame.display.update()
        clock.tick(25000)


game_intro()
game_loop()
pygame.quit()
quit()
