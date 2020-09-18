from pygame.locals import *
import pygame
import os
from glob import glob
import pickle
from time import time
from tkinter import filedialog



'''
creating a list of images in the folders:
imgs1 for layer = "1"
imgs2 ...
imgs3 ...
imgs4 ...

'''

folder = "imgs"
listtiles2 = [x for x in glob(folder + "1\\*.png")]
listtiles1 = [x for x in glob(folder + "2\\*.png")]
listtiles0 = [x for x in glob(folder + "3\\*.png")]
listtiles00 = [x for x in glob(folder + "4\\*.png")]


'''
This create 4 lists with the surfaces with images from imgs1/ .... imgs4/


'''


def load_images():
    "List of surfaces for layer 1 2 3 4"
    til1 = [pygame.image.load(x) for x in listtiles2]
    tile2 = [pygame.image.load(x) for x in listtiles1]
    tile3 = [pygame.image.load(x) for x in listtiles0]
    tile4 = [pygame.image.load(x) for x in listtiles00]
    return til1, tile2, tile3, tile4


'''

                    makes some globals


                    tile1.... 4


'''


def init_display():
    "Initializing pygame, fonts... display and screen"
    global screen, til1, tile2, tile3, tile4, display
    global WINDOW_SIZE, cnt, clock, text
    global font

    pygame.init()
    font = pygame.font.SysFont("Arial", 12)
    WINDOW_SIZE = (464 * 3, 256 * 3)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((464, 256))
    til1, tile2, tile3, tile4 = load_images()
    text = font.render("Pygame MAP EDITOR", 0, (222, 255, 0))
    clock = pygame.time.Clock()




def blit_tiles(mp1):
    "Display all the bricks, called by while loop"

    global tile, letters

    associations = [
        [map1, til1, latters1],
        [map2, tile2, letters2],
        [map3, tile3, letters3],
        [map4, tile4, letters4]]


    '''
    blip the tiles....
    each frame it blips all the tiles for all the layers
    this needs to be optimized?
    '''

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
    map2 = [
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
    return map2


#map3[0][0] = "w"

pygame.init()
init_display()
pos = x, y = pygame.mouse.get_pos()


# This is to give a different name to every screenshot saved
# based on the num of file in the folder
num_file = len(os.listdir())
map_name = f"map{num_file}.png"



# This places a brick or a tile when hit button left
# deletes bricks/blit_tiles when hit button right
def place_block(actual_tile, x, y, mp):
    "Place a tile where the mouse is, the tile is passed"
    x, y = get_x_y()
    mp[y][x] =  actual_tile


def copy_block(x, y, mp):
    "Press c and it copies the tile at the mouse position"
    x, y = get_x_y()
    # gets the number in the layer representing that tile
    copied_tile_id = mp[y][x]
    # return
    return copied_tile_id


def get_x_y():
    "Returns col and row of the tile in the mouse pos being in a ration of 48 pixel for col/row"
    x, y = pygame.mouse.get_pos()
    pos = x, y = x // 48, y // 48
    return pos


def save_map():
    with open("map1.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open("map2.pkl", "wb") as file:
        pickle.dump(map2, file)
    with open("map3.pkl", "wb") as file:
        pickle.dump(map3, file)
    with open("map4.pkl", "wb") as file:
        pickle.dump(map4, file)


def store_maps():
    tm = time()
    with open(f"pkl\\map1.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open(f"pkl\\map2.pkl", "wb") as file:
        pickle.dump(map2, file)
    with open(f"pkl\\map3.pkl", "wb") as file:
        pickle.dump(map3, file)
    with open(f"pk\\map4.pkl", "wb") as file:
        pickle.dump(map4, file)


def load_map(filename, mp1):
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    else:
        mp = mp1
    return mp





def show_tiles_num(cnt, x, y):
    xnum = font.render(str(layer) + ") " + str(cnt), 1, pygame.Color("White"))
    display.blit(xnum, (x-30, y))


def pointer_tiles():
    # =========== SHOW TILE NEXT THE POINTER ===========
    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 3, y // 3
    if layer == "1":
        show_tiles_num(cnt1, x, y)
        display.blit(til1[cnt1], (x, y))
    elif layer == "2":
        show_tiles_num(cnt2, x, y)
        display.blit(tile2[cnt2], (x, y))
    elif layer == "3":
        show_tiles_num(cnt3, x, y)
        display.blit(tile3[cnt3], (x, y))
    elif layer == "4":
        show_tiles_num(cnt4, x, y)
        display.blit(tile4[cnt4], (x, y))
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


#               G L O B A L    S C O P E
# Letter used for the blit_tiles, automatically chosen depending on the images in folder imgs
# just add images in the folder imgs and the code will assign a letter
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

latters1 = [x for x in range(len(til1))]
letters2 = [x for x in range(len(tile2))]
letters3 = [x for x in range(len(tile3))]
letters4 = [x for x in range(len(tile4))]
# Create the map

if any([
    "map4.pkl",
    "map3.pkl",
    "map2.pkl",
    "map1.pkl"]) not in os.listdir():
    map1 = map_to_list()
    map2 = map_to_list()
    map3 = map_to_list()
    map4 = map_to_list()

map4 = load_map("map4.pkl", map4)
map3 = load_map("map3.pkl", map3)
map2 = load_map("map2.pkl", map2)
map1 = load_map("map1.pkl", map1)

# print(map1)

layer = "1"

# This are used to toggle layers
show_layer4 = 1
show_layer3 = 1
show_layer2 = 1
show_layer1 = 1


loop = 1
while loop:
    # clear and  
    display.fill((25, 75, 150))
    if show_layer4:
        blit_tiles(map4)
    if show_layer3:
        blit_tiles(map3)
    if show_layer2:
        blit_tiles(map2)
    if show_layer1:
        blit_tiles(map1)
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
                if layer == "1":
                    cnt1 = copy_block(x, y, map1)
                if layer == "2":
                    cnt2 = copy_block(x, y, map2)
                if layer == "3":
                    cnt3 = copy_block(x, y, map3)
                if layer == "4":
                    cnt4 = copy_block(x, y, map4)

            
            # toggle layers ============================ 1.5

            if event.key == K_l:
                show_layer1 = False if show_layer1 else True
            if event.key == K_k:
                show_layer2 = False if show_layer2 else True
            if event.key == K_j:
                show_layer3 = False if show_layer3 else True
            if event.key == K_h:
                show_layer4 = False if show_layer4 else True

            # Shows mouse position =======================
            if event.key == K_m:
                x, y = pygame.mouse.get_pos()
                text = font.render(f"{x},{y}", 1, (244, 0, 0))


            # DELETE THE SINGLE LAYERS

            if event.key == K_1:
                map1 = map_to_list()
            if event.key == K_2:
                map2 = map_to_list()
            if event.key == K_3:
                map3 = map_to_list()
            if event.key == K_4:
                map4 = map_to_list()


            ################### CHANGE LAYER ########################
            #                       p, o, i, u shows the 4 tiles and set the layer

            if event.key == K_p:
                layer = "1"
                text = font.render("Layer 1 ............. 1p 2o 3i 4u", 1, (222, 0, 0))

            elif event.key == K_o:
                layer = "2"
                text = font.render("Layer 2 ............... 1p 2o 3i 4u", 1, (222, 222, 0))
            elif event.key == K_i:
                layer = "3"
                text = font.render("Layer 3 ............... 1p 2o 3i 4u", 1, (0, 222, 222))
            elif event.key == K_u:
                layer = "4"
                text = font.render("Layer 4 ................. 1p 2o 3i 4u", 1, (0, 222, 222))


        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            if layer == "1":
                place_block(latters1[cnt1], x, y, map1)
            elif layer == "2":
                place_block(letters2[cnt2], x, y, map2)
            elif layer == "3":
                place_block(letters3[cnt3], x, y, map3)
            elif layer == "4":
                place_block(letters4[cnt4], x, y, map4)

        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
                    if layer == "1":
                        place_block(0, x, y, map1)
                    elif layer == "2":
                        place_block(0, x, y, map2)
                    elif layer == "3":
                        place_block(0, x, y, map3)
                    elif layer == "4":
                        place_block(0, x, y, map4)
        
        # M O U S E    W H E E L

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if layer == "1":
                    cnt1 = tilesrollup(cnt1, latters1)
                if layer == "2":
                    cnt2 = tilesrollup(cnt2, letters2)
                if layer == "3":
                    cnt3 = tilesrollup(cnt3, letters3)
                if layer == "4":
                    cnt4 = tilesrollup(cnt4, letters4)

            if event.button == 5:
                if layer == "1":
                    cnt1 = tilesrolldown(cnt1, latters1)
                if layer == "2":    
                    cnt2 = tilesrolldown(cnt2, letters2)
                if layer == "3":
                    cnt3 = tilesrolldown(cnt3, letters3)
                if layer == "4":
                    cnt4 = tilesrolldown(cnt4, letters4)


    pointer_tiles()
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(30)

pygame.quit()