from pygame.locals import *
import pygame
import os
from glob import glob
import pickle
from time import time
from tkinter import filedialog


def load_images(folder):
    "creates 4 list of images/surfaces for the 4 layers"
    listtiles2 = [x for x in glob(folder + "2\\*.png")]
    listtiles1 = [x for x in glob(folder + "1\\*.png")]
    listtiles0 = [x for x in glob(folder + "0\\*.png")]
    listtiles00 = [x for x in glob(folder + "00\\*.png")]
    tile20 = [pygame.image.load(x) for x in listtiles2]
    tile1 = [pygame.image.load(x) for x in listtiles1]
    tile0 = [pygame.image.load(x) for x in listtiles0]
    tile00 = [pygame.image.load(x) for x in listtiles00]
    return tile20, tile1, tile0, tile00


def init_display():
    "Initializing pygame, fonts... display and screen"
    global screen, tile20, tile1, tile0, tile00, display
    global WINDOW_SIZE, cnt, clock, text
    global font

    pygame.init()
    font = pygame.font.SysFont("Arial", 12)
    WINDOW_SIZE = (464 * 3, 256 * 3)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((464, 256))
    tile20, tile1, tile0, tile00 = load_images("imgs")
    text = font.render("Pygame MAP EDITOR", 0, (222, 255, 0))
    clock = pygame.time.Clock()


cnt1 = 0
cnt2 = 0
cnt0 = 0
cnt00 = 0

def blit_tiles(mp1):
    "Display all the bricks, called by while loop"

    global tile, letters

    associations = [
        [map2, tile20, letters2],
        [map1, tile1, letters1],
        [map0, tile0, letters0],
        [map00, tile00, letters00]]

    for assoc in associations:
        if mp1 == assoc[0]:
            tile, letters = assoc[1:]


    for y, line in enumerate(mp1):
        # for each carachter 
        for x, c in enumerate(line):
            for n in letters:
                if c != 0:
                    display.blit(tile[c], (x * 16, y * 16))


def map_to_list():
    "Creates a list of 16 lists with 29 empty spaces as items"
    map1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    return map1


#map0[0][0] = "w"

pygame.init()
init_display()
pos = x, y = pygame.mouse.get_pos()
# letter = "spazio"
num_file = len(os.listdir())
map_name = f"map{num_file}.png"



# This places a brick or a tile when hit button left
# deletes bricks/blit_tiles when hit button right
def place_block(actual_tile, x, y, mp):
    x, y = get_x_y()
    mp[y][x] =  actual_tile

def copy_block(x, y, mp):
    x, y = get_x_y()
    # gets the number in the layer representing that tile
    copied_tile_id = mp[y][x]
    # return
    return copied_tile_id


def get_x_y():
    x, y = pygame.mouse.get_pos()
    pos = x, y = x // 48, y // 48
    return pos


def save_map():
    with open("map2.pkl", "wb") as file:
        pickle.dump(map2, file)
    with open("map1.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open("map0.pkl", "wb") as file:
        pickle.dump(map0, file)
    with open("map00.pkl", "wb") as file:
        pickle.dump(map00, file)


def store_maps():
    tm = time()
    with open(f"pkl\\map2.pkl", "wb") as file:
        pickle.dump(map2, file)
    with open(f"pkl\\map1.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open(f"pkl\\map0.pkl", "wb") as file:
        pickle.dump(map0, file)
    with open(f"pk\\map00.pkl", "wb") as file:
        pickle.dump(map00, file)


def load_map(filename, mp1):
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    else:
        mp = mp1
    return mp


# Letter used for the blit_tiles, automatically chosen depending on the images in folder imgs
# just add images in the folder imgs and the code will assign a letter

letters2 = [x for x in range(len(tile20))]
letters1 = [x for x in range(len(tile1))]
letters0 = [x for x in range(len(tile0))]
letters00 = [x for x in range(len(tile00))]
# Create the map

map2 = map_to_list()
map1 = map_to_list()
map0 = map_to_list()
map00 = map_to_list()

map00 = load_map("map00.pkl", map00)
map0 = load_map("map0.pkl", map0)
map1 = load_map("map1.pkl", map1)
map2 = load_map("map2.pkl", map2)

print(map2)

layer = "2"


def show_tiles_num(cnt, x, y):
    xnum = font.render(str(layer) + ") " + str(cnt), 1, pygame.Color("White"))
    display.blit(xnum, (x-30, y))


def pointer_tiles():
    # =========== SHOW TILE NEXT THE POINTER ===========
    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 3, y // 3
    if layer == "2":
        show_tiles_num(cnt2, x, y)
        display.blit(tile20[cnt2], (x, y))
    elif layer == "1":
        show_tiles_num(cnt1, x, y)
        display.blit(tile1[cnt1], (x, y))
    elif layer == "0":
        show_tiles_num(cnt0, x, y)
        display.blit(tile0[cnt0], (x, y))
    elif layer == "00":
        show_tiles_num(cnt00, x, y)
        display.blit(tile00[cnt00], (x, y))
    # ==================================================

def tilesrollup(cnt, letters):
    cnt += 1
    if cnt > len(letters) - 1:
        cnt = 0
    return cnt


def tilesrolldown(cnt, letters):
    cnt -= 1
    if cnt < 0:
        cnt = len(letters) - 1
    return cnt


show_layer00 = 1
show_layer0 = 1
show_layer1 = 1
show_layer2 = 1


loop = 1
while loop:
    # clear and  
    display.fill((25, 75, 150))
    if show_layer00:
        blit_tiles(map00)
    if show_layer0:
        blit_tiles(map0)
    if show_layer1:
        blit_tiles(map1)
    if show_layer2:
        blit_tiles(map2)
    display.blit(text, (0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            save_map()
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                save_map()
                loop = 0
            # Save screen with 's'
            if event.key == K_s:
                pygame.image.save(screen, map_name)
                os.startfile(map_name)
            
            if event.key == K_c:
                if layer == "2":
                    cnt2 = copy_block(x, y, map2)
                if layer == "1":
                    cnt1 = copy_block(x, y, map1)
                if layer == "0":
                    cnt0 = copy_block(x, y, map0)
                if layer == "00":
                    cnt00 = copy_block(x, y, map00)

            
            # toggle layers ============================ 1.5

            if event.key == K_l:
                show_layer2 = False if show_layer2 else True
            if event.key == K_k:
                show_layer1 = False if show_layer1 else True
            if event.key == K_j:
                show_layer0 = False if show_layer0 else True
            if event.key == K_h:
                show_layer00 = False if show_layer00 else True

            # Shows mouse position =======================
            if event.key == K_m:
                x, y = pygame.mouse.get_pos()
                text = font.render(f"{x},{y}", 1, (244, 0, 0))


            if event.key == K_1:
                map2 = map_to_list()
            if event.key == K_2:
                map1 = map_to_list()
            if event.key == K_3:
                map0 = map_to_list()
            if event.key == K_4:
                map00 = map_to_list()


            ################### CHANGE LAYER ########################
            #                       p, o, i, u shows the 4 tiles and set the layer

            if event.key == K_p:
                layer = "2"
                text = font.render("Layer 1 ............. 1p 2o 3i 4u", 1, (222, 0, 0))


            elif event.key == K_o:
                layer = "1"
                text = font.render("Layer 2 ............... 1p 2o 3i 4u", 1, (222, 222, 0))
            elif event.key == K_i:
                layer = "0"
                text = font.render("Layer 3 ............... 1p 2o 3i 4u", 1, (0, 222, 222))
            elif event.key == K_u:
                layer = "00"
                text = font.render("Layer 4 ................. 1p 2o 3i 4u", 1, (0, 222, 222))


        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            if layer == "2":
                place_block(letters2[cnt2], x, y, map2)
            elif layer == "1":
                place_block(letters1[cnt1], x, y, map1)
            elif layer == "0":
                place_block(letters0[cnt0], x, y, map0)
            elif layer == "00":
                place_block(letters00[cnt00], x, y, map00)

        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
                    if layer == "2":
                        place_block(0, x, y, map2)
                    elif layer == "1":
                        place_block(0, x, y, map1)
                    elif layer == "0":
                        place_block(0, x, y, map0)
                    elif layer == "00":
                        place_block(0, x, y, map00)
        
        # Choose tiles scrolling the middle mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if layer == "2":
                    cnt2 = tilesrollup(cnt2, letters2)
                if layer == "1":
                    cnt1 = tilesrollup(cnt1, letters1)
                if layer == "0":
                    cnt0 = tilesrollup(cnt0, letters0)
                if layer == "00":
                    cnt00 = tilesrollup(cnt00, letters00)
            if event.button == 5:
                if layer == "2":
                    cnt2 = tilesrolldown(cnt2, letters2)

                if layer == "1":    
                    cnt1 = tilesrolldown(cnt1, letters1)

                if layer == "0":
                    cnt0 = tilesrolldown(cnt0, letters0)
                if layer == "00":
                    cnt00 = tilesrolldown(cnt00, letters00)


    pointer_tiles()
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(30)

pygame.quit()