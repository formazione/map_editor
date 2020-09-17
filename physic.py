# phisyc.py
import pygame
import sys


pygame.init()
WSIZE = (0, 0)
screen = pygame.display.set_mode(WSIZE)
W, H = screen.get_size()
print(W, H)
clock = pygame.time.Clock()

loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0

    pygame.display.update()
    clock.tick(60)



pygame.quit()
sys.exit()