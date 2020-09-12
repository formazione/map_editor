# theflash
import pygame
from pygame.locals import *
import pickle
import os
import sys
from glob import glob


pygame.init()
WSIZE = (928, 512)
screen = pygame.display.set_mode((WSIZE))
W, H = WSIZE
display = pygame.Surface((W // 2, H // 2))
clock = pygame.time.Clock()



def load_images(folder):
    # This has things to overlay onto layer 1
    listtiles2 = [x for x in glob(folder + "2\\*.png")]
    tile2 = [pygame.image.load(x) for x in listtiles2]
    return tile2


def load_map(filename, mp1):
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    else:
        mp = mp1
    return mp


def showmap(mp1):
    for y, line in enumerate(mp1):
        for x, c in enumerate(line):
            for n, l in enumerate(letters):
                if c == l:
                    display.blit(tile[n], (x * 16, y * 16))

# def map_to_list():
#     "Creates a list of 16 lists with 29 empty spaces as items"
#     map1 = []
#     for x in range(16):
#         line = [x for x in "                             "]
#         map1.append(line)
#     return map1

tile = load_images("imgs")
alphab = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.,:;@#°^[]<>()&%$£€ABC1234567890òàèéù+-ì={}§!?/|"
letters = [x for x in alphab[0:len(tile)]]
map2 = []
map2 = load_map("last_map2.pkl", map2)

# print(map2)
# showmap(map2)

loop = 1
showmap(map2)
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                loop = 0

    screen.blit(pygame.transform.scale(display, WSIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()