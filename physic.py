# phisyc.py
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

