from pygame.locals import *
import pygame
import os
from glob import glob
import pickle
from list_box_tut import *
from time import time
from tkinter import filedialog

# map editor 1.3
'''
tile
    list with surfaces with images (bricks)

tiles(map1)
    displays all the tiles depending on the letters in the map1 list

map_to_list()
    creates the first template of the map

letters
    a list of letters, same number as the images in folder imgs\
    You can add an image and it will be assigned a letter by the code without having to change the code

'''

def load_images(folder):
    listtiles1 = [x for x in glob(folder + "1\\*.png")]
    listtiles0 = [x for x in glob(folder + "0\\*.png")]
    listtiles00 = [x for x in glob(folder + "00\\*.png")]
    tile1 = [pygame.image.load(x) for x in listtiles1]
    tile0 = [pygame.image.load(x) for x in listtiles0]
    tile00 = [pygame.image.load(x) for x in listtiles00]
    return tile1, tile0, tile00



def init_display():
    global screen, tile1, tile0, tile00, display
    global WINDOW_SIZE, cnt, clock, text
    global font

    pygame.init()
    font = pygame.font.SysFont("Arial", 20)
    WINDOW_SIZE = (464 * 2, 256 * 2)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    tile1, tile0, tile00 = load_images("imgs")
    text = font.render("Layer 1", 1, (222, 0, 0))
    clock = pygame.time.Clock()


cnt1 = 0
cnt0 = 0
cnt00 = 0


def blit_tiles(mp1):
    "Display all the bricks, called by while loop"

    global tile, letters

    if mp1 == map1:
        tile = tile1
        letters = letters1
    if mp1 == map0:
        tile = tile0
        letters = letters0
    if mp1 == map00:
        tile = tile00
        letters = letters00

    for y, line in enumerate(mp1):
        for x, c in enumerate(line):
            for n, l in enumerate(letters):
                if c == l:
                    display.blit(tile[n], (x * 16, y * 16))
"""
map00 = [
[" ", "A", " ", " ".... " "],
[" ", "A", " ", " ".... " "],
[" ", "A", " ", " ".... " "],
...

]



"""


def map_to_list():
    "Creates a list of 16 lists with 29 empty spaces as items"
    map1 = []
    for x in range(16):
        line = [x for x in "                             "]
        map1.append(line)
    return map1

# Create the map
map1 = map_to_list()
map0 = map_to_list()
map00 = map_to_list()

#map0[0][0] = "w"

pygame.init()
init_display()
last_pos = x, y = pygame.mouse.get_pos()
letter = "spazio"
num_file = len(os.listdir())
map_name = f"map{num_file}.png"

# Letter used for the blit_tiles, automatically chosen depending on the images in folder imgs
# just add images in the folder imgs and the code will assign a letter
alphab = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.,:;@#°^[]<>()&%$£€ABC1234567890òàèéù+-ì={}§!?/|"
letters1 = [x for x in alphab[0:len(tile1)]]
letters0 = [x for x in alphab[0:len(tile0)]]
letters00 = [x for x in alphab[0:len(tile00)]]


# This places a brick or a tile when hit button left
# deletes bricks/blit_tiles when hit button right
def place_block(actual_tile, x, y, mp):
    x, y = get_x_y()
    mp[y][x] =  actual_tile


def get_x_y():
    x, y = pygame.mouse.get_pos()
    pos = x, y = x // 32, y // 32
    return pos

def save_last_map():

    with open("last_map.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open("last_map0.pkl", "wb") as file:
        pickle.dump(map0, file)
    with open("last_map00.pkl", "wb") as file:
        pickle.dump(map00, file)

def save_map():
    tm = time()
    with open(f"pkl\\map{time}.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open(f"pkl\\mao{time}0.pkl", "wb") as file:
        pickle.dump(map0, file)
    with open(f"pk\\map{time}00.pkl", "wb") as file:
        pickle.dump(map00, file)


def load_last_map(filename):
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    return mp


map00 = load_last_map("last_map00.pkl")
map0 = load_last_map("last_map0.pkl")
map1 = load_last_map("last_map.pkl")
layer = "1"

loop = 1
while loop:
    # clear and  
    display.fill((0, 0, 0))
    blit_tiles(map00)
    blit_tiles(map0)
    blit_tiles(map1)
    display.blit(text, (0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            save_last_map()
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                save_last_map()
                loop = 0
            # Save screen with 's'
            if event.key == K_s:
                pygame.image.save(screen, map_name)
                # os.startfile(map_name)

            # if event.key == K_l:
            #     filename = filedialog.askopenfilename(initialdir = "\\pkl",title = "Select file",filetypes = (("pickle files","*.pkl"),("all files","*.*")))
            #     map1 = load_map(filename)
            #     map0 = load_map(filename[:-4] + "0" + ".pkl")
            #     map00 = load_map(filename[:-4] + "00" + ".pkl")


            # if event.key == K_m:
            #     show_menu()

            # Delete all wit 'd'
            if event.key == K_1:
                map1 = map_to_list()
            if event.key == K_2:
                map0 = map_to_list()
            if event.key == K_3:
                map00 = map_to_list()


            ################### CHANGE LAYER ########################
            
            if event.key == K_p:
                layer = "1"
                text = font.render("Layer 1", 1, (222, 0, 0))
            elif event.key == K_o:
                layer = "0"
                text = font.render("Layer 0", 1, (222, 222, 0))
            elif event.key == K_i:
                layer = "00"
                text = font.render("Layer 00", 1, (0, 222, 222))

            # elif event.key == K_a:
            #     place_block(letters[cnt], x, y, map0)
            #     if pygame.mouse.get_pressed()[2]:
            #         place_block(" ", x, y, map0)

            # elif event.key == K_z:
            #     place_block(letters[cnt], x, y, map00)
            #     if pygame.mouse.get_pressed()[2]:
            #         place_block(" ", x, y, map00)

        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            if layer == "1":
                place_block(letters1[cnt1], x, y, map1)
            if layer == "0":
                place_block(letters0[cnt0], x, y, map0)
            if layer == "00":
                place_block(letters00[cnt00], x, y, map00)

        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
                    if layer == "1":
                        place_block(" ", x, y, map1)
                    if layer == "0":
                        place_block(" ", x, y, map0)
                    if layer == "00":
                        place_block(" ", x, y, map00)
        
        # Choose tiles scrolling the middle mouse wheel




        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if layer == "1":
                    letters = letters1
                    cnt1 += 1
                    if cnt1 > len(letters1) - 1:
                        cnt1 = 0
                    cnt = cnt1
                    print(cnt)
                if layer == "0":
                    letters = letters0
                    cnt0 += 1
                    if cnt0 > len(letters0) - 1:
                        cnt0 = 0
                    cnt = cnt0
                if layer == "00":
                    letters = letters00
                    cnt00 += 1
                    if cnt00 > len(letters00) - 1:
                        cnt00 = 0
                    cnt = cnt00


                # if cnt > len(letters) - 1:
                #     cnt = 0
            if event.button == 5:
                if layer == "1":
                    letters = letters1
                    cnt1 -= 1
                    if cnt1 < 0:
                        cnt1 = len(letters1) - 1
                    cnt = cnt1
                    print(cnt)
                if layer == "0":
                    letters = letters0
                    cnt0 -= 1
                    if cnt0 < 0:
                        cnt0 = len(letters0) - 1
                    cnt = cnt0
                if layer == "00":
                    letters = letters00
                    cnt00 -= 1
                    if cnt00 < 0:
                        cnt00 = len(letters00) -1
                    cnt = cnt00

    # =========== SHOW TILE NEXT THE POINTER ===========
    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 2, y // 2
    if layer == "1":
        display.blit(tile1[cnt1], (x, y))
    if layer == "0":
        display.blit(tile0[cnt0], (x, y))
    if layer == "00":
        display.blit(tile00[cnt00], (x, y))
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(30)
pygame.quit()