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

My_Image = pygame.image.load('link.png')

R = My_Image.get_rect()

D2R = (math.pi * 2) / 360
Direction_Vector_Lookup = list([[math.cos(D2R * degrees), math.sin(D2R * degrees)] for degrees in range(360)])

direction = 1

x = DW_Half - R.center[0]
y = DH_Half - R.center[0]


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


while True:
    event_handler()

    DS.blit(My_Image, (x, DH_Half - R.center[1]))

    x += direction
    #y += direction

    if x >= Display_Width - R.width or x <= 0:
        direction *= -1
    #if x >= Display_Height - R.height or x <= 0:
     #   direction += -1

    pygame.display.update()
    DS.fill([0, 0, 0])
