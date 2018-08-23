import pygame
import sys
import math
import random
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

Display_Width = 1280
Display_Height = 720
DW_Half = Display_Width / 2
DH_Half = Display_Height / 2
Display_Area = Display_Width * Display_Height
DS = pygame.display.set_mode((Display_Width, Display_Height))

Ball = pygame.image.load('link.png')

R = Ball.get_rect()

D2R = (math.pi * 2) / 360
Direction_Vector_Lookup = list([[math.cos(D2R * degrees), math.sin(D2R * degrees)] for degrees in range(360)])


class ball():
    x = 0.0
    y = 0.0

    def __init__(self, r=R):
        global Display_Width, Display_Height, Direction_Vector_Lookup
        self.r = r
        self.x = random.randint(r.center[0], Display_Width - r.center[0])
        self.y = random.randint(r.center[1], Display_Height - r.center[1])
        self.x += random.randint(r.center[0], Display_Width - r.center[0])
        self.y += random.randint(r.center[1], Display_Height - r.center[1])
        self.dx, self.dy = Direction_Vector_Lookup[random.randint(0, 359)]

    def draw(self, ds=DS, image=Ball):
        ds.blit(image, (self.x - self.r.center[0], self.y - self.r.center[1]))

    def move(self):
        global Display_Width, Display_Height
        self.x += self.dx
        self.y += self.dy
        if self.x <= self.r.center[0] or self.x >= Display_Width - self.r.center[0]:
            self.dx = -self.dx
        if self.y <= self.r.center[1] or self.y >= Display_Height - self.r.center[1]:
            self.dy = -self.dy

    def do(self):
        self.move()
        self.draw()


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


nBALLS = 20
BALLS = list([ball() for count in range(nBALLS)])

while True:
    event_handler()

    for b in BALLS:
        b.do()

    pygame.display.update()
    DS.fill([0, 0, 0])
