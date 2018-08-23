import pygame, sys, time
from pygame.locals import *

pygame.init()

Display_Width = 800
Display_Height = 600
DW_Half = Display_Width / 2
DH_Half = Display_Height / 2
Display_Area = Display_Width * Display_Height
DS = pygame.display.set_mode((Display_Width, Display_Height))
x = 0
y = 0

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()









while True:

    if event.type == KEYDOWN:
        if event.key == K_w:

    event_handler()
    pygame.display.update()
    DS.fill([0, 0, 0])
