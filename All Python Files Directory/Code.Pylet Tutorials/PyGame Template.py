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

    pygame.display.update()
    DS.fill([0, 0, 0])
