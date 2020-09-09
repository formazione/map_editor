from pygame.locals import *
import pygame
import os
from glob import glob
import pickle


# map editor 1.2
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

def init_display():
    global screen, tile, display, WINDOW_SIZE, cnt, clock

    pygame.init()
    WINDOW_SIZE = (464*2, 256*2)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

    listtiles = [x for x in glob("imgs\\*.png")]
    tile = [pygame.image.load(x) for x in listtiles]
    clock = pygame.time.Clock()


cnt = 0
def blit_tiles(mp1):
    "Display all the bricks, called by while loop"

    global tile, letters

    for y, line in enumerate(mp1):
        for x, c in enumerate(line):
            for n, l in enumerate(letters):
                if c == l:
                    display.blit(tile[n], (x * 16, y * 16))



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

map0[0][0] = "w"

pygame.init()
init_display()
loop = 1
last_pos = x, y = pygame.mouse.get_pos()
letter = "spazio"
num_file = len(os.listdir())
map_name = f"map{num_file}.png"

# Letter used for the blit_tiles, automatically chosen depending on the images in folder imgs
# just add images in the folder imgs and the code will assign a letter
alphab = "qwertyuiopasdfghjklzxcvbnm.,:;@#°^[]<>()&%$£€"
letters = [x for x in alphab[:len(tile)]]


# This places a brick or a tile when hit button left
# deletes bricks/blit_tiles when hit button right
def place_block(actual_tile, x, y, mp):
    x, y = pygame.mouse.get_pos()
    x, y = x // 32, y // 32
    mp[y][x] =  actual_tile




def save_last_map():

    with open("last_map.pkl", "wb") as file:
        pickle.dump(map1, file)
    with open("last_map0.pkl", "wb") as file:
        pickle.dump(map0, file)
    with open("last_map00.pkl", "wb") as file:
        pickle.dump(map00, file)

def load_last_map(mp):
    if mp == map1:
        filename = "last_map.pkl"
    elif mp == map0:
        filename = "last_map0.pkl"
    elif mp == map00:
        filename = "last_map00.pkl"

    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    return mp



map00 = load_last_map(map00)
map0 = load_last_map(map0)
map1 = load_last_map(map1)
while loop:
    # clear and  
    display.fill((0, 0, 0))
    blit_tiles(map00)
    blit_tiles(map0)
    blit_tiles(map1)
    
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
                os.startfile(map_name)

            if event.key == K_l:
                map1 = load_last_map(map1)
                map0 = load_last_map(map0)

            # Delete all wit 'd'
            if event.key == K_d:
                map1 = map_to_list()
                map0 = map_to_list()
                map00 = map_to_list()

            elif event.key == K_a:
                place_block(letters[cnt], x, y, map0)
                if pygame.mouse.get_pressed()[2]:
                    place_block(" ", x, y, map0)

            elif event.key == K_z:
                place_block(letters[cnt], x, y, map00)
                if pygame.mouse.get_pressed()[2]:
                    place_block(" ", x, y, map00)


        # Place block with left mouse button
        if pygame.mouse.get_pressed()[0]:
            place_block(letters[cnt], x, y, map1)



        # Place empty space with right mouse button
        elif pygame.mouse.get_pressed()[2]:
            place_block(" ", x, y, map1)
        
        # Choose tiles scrolling the middle mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                print(event.button)
                cnt += 1
                if cnt > len(letters) - 1:
                    cnt = 0
            if event.button == 5:
                cnt -= 1
                if cnt < 0:
                    cnt = len(letters) - 1


    x, y = pygame.mouse.get_pos()
    x -= 14
    y -= 14
    x, y = x // 2, y // 2
    display.blit(tile[cnt], (x, y))
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()