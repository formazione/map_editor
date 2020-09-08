from pygame.locals import *
import pygame
import os
from glob import glob

# map editor 1.2

def init_display():
    global screen, tile, display, WINDOW_SIZE, cnt, clock

    pygame.init()
    WINDOW_SIZE = (464*2, 256*2)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

    listtiles = [x for x in glob("imgs\\brick*.png")]
    tile = [pygame.image.load(x) for x in listtiles]
    clock = pygame.time.Clock()
    print(tile)

cnt = 0
def tiles(map1):
    global tile, letters
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            for n, l in enumerate(letters):
                if c == l:
                    display.blit(tile[n], (x * 16, y * 16))
            # elif c == "y":
            #     display.blit(tile[1], (x * 16, y * 16))
            # elif c == "c":
            #     display.blit(tile[2], (x * 16, y * 16))
            # # add a new letter for each images


def map_to_list():
    start = "w"*29
    map1 = "w" + " " * 27 + "w\n"
    map1 = start + map1 * 14 + start
    map1 = map1.splitlines()
    map2 = []
    for n, line in enumerate(map1):
        map2.append(list(map1[n]))
    print(*map2, sep="\n")
    return map2


map1 = map_to_list()

pygame.init()
init_display()
loop = 1
last_pos = x, y = pygame.mouse.get_pos()
letter = "spazio"
num_file = len(os.listdir())
map_name = f"map{num_file}.png"

# Add a letter for each tile in imgs\
alphab = "qwertyuiopasdfghjklzxcvbnm"
letters = [x for x in alphab[:len(tile)]]


def place_block(actual_tile, x, y):
    x, y = pygame.mouse.get_pos()
    # You divide by 32 for its scaled (pygame.transform.scale)
    x, y = int(x / 32), int(y / 32)
    map1[y][x] = actual_tile

while loop:
    # clear and  
    display.fill((0, 0, 0))
    tiles(map1)

    
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:

            # Save screen with 's'
            if event.key == K_s:
                pygame.image.save(screen, map_name)
                os.startfile(map_name)

            # Delete all wit 'd'
            if event.key == K_d:
                map1 = map_to_list()

        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            place_block(letters[cnt], x, y)
        
        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
            place_block(" ", x, y)
        
        # Change the tile scrolling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                print(event.button)
                cnt += 1
                if cnt > len(letters) - 1:
                    cnt = 0
            print(cnt)


    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 2, y // 2
    display.blit(tile[cnt], (x, y))
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()