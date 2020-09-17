# phisyc.py
import pygame
import sys


pygame.init()
WSIZE = (600, 500)
screen = pygame.display.set_mode(WSIZE)
# W, H = screen.get_size()
# print(W, H)
clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.size = w, h
        self.image = pygame.Surface(self.size)
        self.image.fill(pygame.Color(color))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        g.add(self)
        print(g)

def gravity(obj):
    obj.rect.top += 2

g = pygame.sprite.Group()
player = Sprite(100, 50, 50, 50, "Red")
bottom = Sprite(0, 490, 600, 10, "Gray")
tile = Sprite(30, 300, 60, 10, "Gray")

moveleft = 0
moveright = 0
fall = 0

loop = 1
while loop:
    if moveright:
        player.rect.right += 1
    if moveleft:
        player.rect.left -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0
            if event.key == pygame.K_LEFT:
                moveright = 0
                moveleft = 1
            if event.key == pygame.K_RIGHT:
                moveleft = 0
                moveright = 1
        if event.type == pygame.KEYUP:
                moveleft = 0
                moveright = 0

    gravity(player)

    pygame.display.update()
    clock.tick(1)



pygame.quit()
sys.exit()