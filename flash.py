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



def load_images(folder: str) -> list:
    "Load tiles from a folder... with a number at the end"
    listtiles2 = [x for x in glob(folder + "2\\*.png")]
    tile2 = [pygame.image.load(x) for x in listtiles2]
    return tile2


def load_map(filename: str, mp1: list):
    "Resume a list with the data (letter) for the tiles to be displayed on display surface"
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    else:
        mp = mp1
    return mp


def showmap(mp1):
    "Take the map list with letters and blit them as tiles on the display surface"
    for y, line in enumerate(mp1):
        for x, c in enumerate(line):
            for n, l in enumerate(letters):
                if c == l:
                    display.blit(tile[n], (x * 16, y * 16))


# calls the function to load tiles from imgs2/
tile = load_images("imgs")
# create a list of all letters corrisponding to the tiles with images from imgs2 folder
alphab = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.,:;@#°^[]<>()&%$£€ABC1234567890òàèéù+-ì={}§!?/|"
letters = [x for x in alphab[0:len(tile)]]
map2 = []
# Stores a list with letters = tiles from pkl file (created with pygame map editor)
map2 = load_map("last_map2.pkl", map2)


loop = 1
# This blit all the tiles on the display surface
showmap(map2)
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                loop = 0
    # the display surface is scaled as the screen (being the half of screen size)
    screen.blit(pygame.transform.scale(display, WSIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()