import sys
import random
import math
import pygame
import pygame.gfxdraw
from pygame.locals import *

FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()

Display_Width = 800
Display_Height = 600
Display_Area = Display_Width * Display_Height
DS = pygame.display.set_mode((Display_Width, Display_Height))

Rectangle_Size = 200
Rect_Mid_200 = (Display_Width / 2 - Rectangle_Size / 2, Display_Height / 2 - Rectangle_Size / 2, Rectangle_Size, Rectangle_Size)

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


while True:
    event_handler()

    #pygame.draw.rect(DS, ORANGE, Rect_Mid_200, 0)

    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    w = random.randint(0, Display_Width - 1)
    h = random.randint(0, Display_Height - 1)
    x = random.randint(0, Display_Width - w)
    y = random.randint(0, Display_Height - h)

    pygame.draw.rect(DS, rgb, (x, y, w, h), 0)

    pygame.display.update()
    DS.fill([0, 0, 0])
