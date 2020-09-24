from pygame.locals import *
import pygame
import os
from glob import glob
import pickle
from time import time
from tkinter import filedialog



'''

save layers in a folder layers/name/layer1.pkl...


'''


class Label:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.surface = font.render(text, 1, pygame.Color("White"))
        self.surface.fill((0,0,0))
        self.set(text, "White")

    def set(self, text, color="White"):
        self.surface = font.render(text, 1, pygame.Color(color))
        size = w, h = self.surface.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.surface2 = pygame.Surface(size)
        self.surface2.blit(self.surface, (0, 0))


def click1(event):

    print("ok")
    show_layer1 = False if show_layer1 else True
    if shos_layer1:
        lab1.set("TOGGLED", "Yellow")



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
    tile1 = [pygame.image.load(x) for x in listtiles2]
    tile2 = [pygame.image.load(x) for x in listtiles1]
    tile3 = [pygame.image.load(x) for x in listtiles0]
    tile4 = [pygame.image.load(x) for x in listtiles00]
    return tile1, tile2, tile3, tile4


'''

                    makes some globals


                    tile1.... 4


'''

pygame.font.init()
font = pygame.font.SysFont("Arial", 11)
def init_display():
    "Initializing pygame, fonts... display and screen"
    global screen, tile1, tile2, tile3, tile4, display
    global WINDOW_SIZE, cnt, clock, text


    pygame.init()
    WINDOW_SIZE = (464 * 3, 256 * 3)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((464, 256))
    tile1, tile2, tile3, tile4 = load_images()
    text = font.render("Pygame MAP EDITOR", 0, (222, 255, 0))
    clock = pygame.time.Clock()




def blit_tiles(mp1):
    "Display all the bricks, called by while loop"

    # global tile, letters

    associations = [
        [layer1, tile1, letters1],
        [layer2, tile2, letters2],
        [layer3, tile3, letters3],
        [layer4, tile4, letters4]]


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

''' Function that start / clear the maps '''


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


#layer3[[0,0]][[0,0]] = "w"




# This places a brick or a tile when hit button left
# deletes bricks/blit_tiles when hit button right
def place_block(actual_tile, x, y, mp):
    "Place a tile where the mouse is, the tile is passed"
    x, y = get_x_y()
    mp[y][x] =  actual_tile


def copy_block(x, y, mp):
    "Press c and it copies the tile at the mouse position"
    x, y = get_x_y()
    copied_tile_id = mp[y][x]
    return copied_tile_id


def get_x_y() -> tuple:
    "Col and Row of mouse pos"
    x, y = pygame.mouse.get_pos()
    pos = x, y = x // 48, y // 48
    return pos


def save_map():
    with open("layer1.pkl", "wb") as file:
        pickle.dump(layer1, file)
    with open("layer2.pkl", "wb") as file:
        pickle.dump(layer2, file)
    with open("layer3.pkl", "wb") as file:
        pickle.dump(layer3, file)
    with open("layer4.pkl", "wb") as file:
        pickle.dump(layer4, file)


def store_maps():
    tm = time()
    with open(f"pkl\\layer1.pkl", "wb") as file:
        pickle.dump(layer1, file)
    with open(f"pkl\\layer2.pkl", "wb") as file:
        pickle.dump(layer2, file)
    with open(f"pkl\\layer3.pkl", "wb") as file:
        pickle.dump(layer3, file)
    with open(f"pk\\layer4.pkl", "wb") as file:
        pickle.dump(layer4, file)


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



def show_tiles():
    "Shows all the tiles of layer1"
    cnt1 = 0
    for n, t in enumerate(tile1):
        display.blit(tile1[cnt1], (x * 16, y * 16))


def pointer_tiles():
    # =========== SHOW TILE NEXT THE POINTER ===========
    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 3, y // 3
    if layer == "1":
        show_tiles_num(cnt1, x, y)
        display.blit(tile1[cnt1], (x, y))
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


pygame.init()
init_display()
pos = x, y = pygame.mouse.get_pos()


# This is to give a different name to every screenshot saved
# based on the num of file in the folder
num_file = len(os.listdir())
map_name = f"map{num_file}.png"

# Counting the tiles for each layer
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0


# Numbers that refers to a tile, this numbers go in the layer1... and are converted to tiles in show tiles

letters1 = [x for x in range(len(tile1))]
letters2 = [x for x in range(len(tile2))]
letters3 = [x for x in range(len(tile3))]
letters4 = [x for x in range(len(tile4))]
# Create the map

# IF there are no files, the map will be empty
if any([
    "layer4.pkl",
    "layer3.pkl",
    "layer2.pkl",
    "layer1.pkl"]) not in os.listdir():
    layer1 = map_to_list()
    layer2 = map_to_list()
    layer3 = map_to_list()
    layer4 = map_to_list()

layer4 = load_map("layer4.pkl", layer4)
layer3 = load_map("layer3.pkl", layer3)
layer2 = load_map("layer2.pkl", layer2)
layer1 = load_map("layer1.pkl", layer1)




layer = "1"

# This are used to toggle layers
show_layer4 = 1
show_layer3 = 1
show_layer2 = 1
show_layer1 = 1

show_tile1 = 1

lab1 = Label("Layer 1", 0, 0)
lab_help = Label("Choose Layers: p o i u - Toggle l k j h - Delete 1 2 3 4", 30, 0)

loop = 1
while loop:
    # clear and  
    display.fill((25, 75, 150))
    
    # SHOW THE LAYERS

    if show_layer4:
        blit_tiles(layer4)
    if show_layer3:
        blit_tiles(layer3)
    if show_layer2:
        blit_tiles(layer2)
    if show_layer1:
        blit_tiles(layer1)

    if show_tile1:
        show_tile1()




    display.blit(text, (0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            save_map()
            loop = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if lab1.rect.collidepoint(mx, my):
                    print("clicked")
                    click1(event)
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
                    cnt1 = copy_block(x, y, layer1)
                if layer == "2":
                    cnt2 = copy_block(x, y, layer2)
                if layer == "3":
                    cnt3 = copy_block(x, y, layer3)
                if layer == "4":
                    cnt4 = copy_block(x, y, layer4)

            
            #                  T O G G L E               #

            if event.key == K_l:
                show_layer1 = False if show_layer1 else True
                layer = "1" if show_layer1 == True else layer
            if event.key == K_k:
                layer = "2"
                show_layer2 = False if show_layer2 else True
                layer = "2" if show_layer2 == True else layer
            if event.key == K_j:
                layer = "3"
                show_layer3 = False if show_layer3 else True
                layer = "3" if show_layer3 == True else layer
            if event.key == K_h:
                layer = "4"
                show_layer4 = False if show_layer4 else True
                layer = "4" if show_layer4 == True else layer


            # =================== SHOW TILES =================

            if event.key == K_m:
                show_tile1 = False if show_tile1 else True
                layer = "1" if show_layer1 == True else layer

            # Shows mouse position =======================
            if event.key == K_m:
                x, y = pygame.mouse.get_pos()
                text = font.render(f"{x},{y}", 1, (244, 0, 0))


            # DELETE THE SINGLE LAYERS

            if event.key == K_1:
                layer1 = map_to_list()
            if event.key == K_2:
                layer2 = map_to_list()
            if event.key == K_3:
                layer3 = map_to_list()
            if event.key == K_4:
                layer4 = map_to_list()


            ################### CHANGE LAYER ########################
            #                       p, o, i, u shows the 4 tiles and set the layer

            if event.key == K_p:
                layer = "1"
                lab1.set("Layer 1")
            elif event.key == K_o:
                layer = "2"
                lab1.set("Layer 2")
            elif event.key == K_i:
                layer = "3"
                lab1.set("Layer 3")
            elif event.key == K_u:
                layer = "4"
                lab1.set("Layer 4")


        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            if layer == "1":
                place_block(letters1[cnt1], x, y, layer1)
            elif layer == "2":
                place_block(letters2[cnt2], x, y, layer2)
            elif layer == "3":
                place_block(letters3[cnt3], x, y, layer3)
            elif layer == "4":
                place_block(letters4[cnt4], x, y, layer4)

        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
                    if layer == "1":
                        place_block(0, x, y, layer1)
                    elif layer == "2":
                        place_block(0, x, y, layer2)
                    elif layer == "3":
                        place_block(0, x, y, layer3)
                    elif layer == "4":
                        place_block(0, x, y, layer4)
        
        # M O U S E    W H E E L

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if layer == "1":
                    cnt1 = tilesrollup(cnt1, letters1)
                if layer == "2":
                    cnt2 = tilesrollup(cnt2, letters2)
                if layer == "3":
                    cnt3 = tilesrollup(cnt3, letters3)
                if layer == "4":
                    cnt4 = tilesrollup(cnt4, letters4)

            if event.button == 5:
                if layer == "1":
                    cnt1 = tilesrolldown(cnt1, letters1)
                if layer == "2":    
                    cnt2 = tilesrolldown(cnt2, letters2)
                if layer == "3":
                    cnt3 = tilesrolldown(cnt3, letters3)
                if layer == "4":
                    cnt4 = tilesrolldown(cnt4, letters4)


    pointer_tiles()
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    screen.blit(lab1.surface, (0, 40))
    screen.blit(lab_help.surface, (0, 50))
    pygame.display.update()
    clock.tick(30)

pygame.quit()