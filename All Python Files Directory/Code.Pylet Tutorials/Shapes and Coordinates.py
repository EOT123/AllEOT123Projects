import pygame
import sys
import math
import random
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

Display_Width = 800
Display_Height = 600
DW_Half = Display_Width / 2
DH_Half = Display_Height / 2
Display_Area = Display_Width * Display_Height
DS = pygame.display.set_mode((Display_Width, Display_Height))


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


while True:
    event_handler()

    #pygame.draw.rect(DS, (255, 255, 255), (250, 250, Display_Width / 2, Display_Height / 2), 1)
    #pygame.draw.rect(DS, (255, 255, 255), (250, 250, Display_Width / 2, Display_Height / 2), 0)

    #pygame.draw.line(DS, (0, 0, 255), (250 + DW_Half / 2, 250), (250 + DW_Half / 2, 250 + DH_Half), 1)
    #pygame.draw.line(DS, (0, 0, 255), (250, 250 + DH_Half / 2), (250 + DW_Half, 250 + DH_Half / 2), 1)
    #pygame.draw.line(DS, (0, 0, 255), (0, 0), (1280, 700), 5)

    # pygame.draw.circle(DS, (255, 255, 255), (Display_Width / 2, Display_Height / 2), 150, 0)

    #pygame.draw.polygon(DS, (255, 255, 255), triangle, 0)
    #pygame.draw.polygon(DS, (255, 255, 255), hexagon, 0)
    #pygame.draw.polygon(DS, (255, 255, 255), octogon, 0)

    pygame.display.update()
    DS.fill([0, 0, 0])
