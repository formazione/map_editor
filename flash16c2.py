import pygame
from glob import glob
import sys
from pygame.locals import *
import os
import pickle


pygame.init()
w, h = WSIZE = ((464 * 3, 256 * 3)) # 1392 x 768
screen = pygame.display.set_mode((w, h))

def load_tiles(folder: str) -> list:
    "Load tiles from a folder... with a number at the end"
    listtiles2 = [x for x in glob(folder + "\\*.png")]
    tile2 = [pygame.image.load(x) for x in listtiles2]
    return tile2


def load_map(filename: str, mp1: list):
    "Check for a map saved in the folder and load it... a bidimentional list of numbers"
    if filename in os.listdir():
        with open(filename, "rb") as file:
            mp = pickle.load(file)
    else:
        mp = mp1
    return mp


tiles_rects = []
def show_layer(layer, tile, temp_surface):
    for y, line in enumerate(layer):
        for x, c in enumerate(line):
            if c != 0:
                temp_surface.blit(tile[c], (x * 16, y * 16))
                tiles_rects.append(Tile(tile[c], x, y))
    return temp_surface


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

# def show_layer(layer, tile):
#     for y, line in enumerate(layer):
#         for x, c in enumerate(line):
#             if c != 0:
#                 temp_surface.blit(tile[c], (x * 16, y * 16))


def show_map():
    "Takes the list with the number associated with tiles and shows the tiles"
    global tile1, tile2

    display = pygame.Surface((464 * 3, 256 * 3))
    temp_surface = pygame.Surface((464, 256))
    # display.fill((0, 0, 0, 0))
    show_layer
    for y, line in enumerate(layer1):
        for x, c in enumerate(line):
            if c != 0:
                temp_surface.blit(tile1[c], (x * 16, y * 16))
    display.blit(pygame.transform.scale(temp_surface, (w, h)), (0, 0))
    Display(display)

def fps():
    "frame rate"
    fr = "Fps: " + str(int(clock.get_fps()))
    frt = font.render(fr, 1, pygame.Color("coral"))
    return frt


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.dogwalking = glob("imgs/walk/*.png")
        self.dogidling = glob("imgs/idle/*.png")
        self.load_images()

    def load(self, x):
        return pygame.transform.scale(pygame.image.load(x).convert_alpha(), (48, 48))

    def flip(self, x):
        return pygame.transform.scale(pygame.transform.flip(self.load(x), 1, 0), (48, 48))

    def load_images(self):
        self.list = [self.load(f) for f in self.dogwalking]
        self.listflip = [self.flip(f) for f in self.dogwalking]
        self.list_idle = [self.load(f) for f in self.dogidling]
        self.list_idleflip = [self.flip(f) for f in self.dogidling]
        self.counter = 0
        self.image = self.list[0]
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.dir = ""
        self.prov = ""
        g.add(self)

    def update_counter(self, vel, img_list):
        self.counter += vel
        if self.counter >= len(img_list):
            self.counter = 0
        self.image = img_list[int(self.counter)]

    def update(self):
        global moveUp, moveLeft, moving_right, moveLeft, faceRight, tiles_rects

        for t in tiles_rects:
            if not t.rect.colliderect(player):
                self.rect.top += 1
        if moving_right:
            self.update_counter(.1, self.list)
            self.prov = self.dir

        if moveLeft:
            self.update_counter(.1, self.listflip)
            # self.image = self.listflip[int(self.counter)]
            self.prov = self.dir

        if self.dir == "":
            self.update_counter(.05, self.list_idle)

            if faceRight:
                self.image = self.list_idleflip[int(self.counter)]

            else:
                self.image = self.list_idle[int(self.counter)]


class Display(pygame.sprite.Sprite):
    def __init__(self, image):
        "Gets the surface of the display with the map and transform it in a map"
        super(Display, self).__init__()
        self.image = image
        wd, hd = self.image.get_size()
        self.rect = pygame.Rect(0, 0, wd, hd)
        g.add(self)


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        "Gets the surface of the display with the map and transform it in a map"
        super(Tile, self).__init__()
        self.image = image
        w, h = self.image.get_size()
        self.rect = pygame.Rect(0, 0, w, h)
        #g.add(self)

# ========================= GLOBAL SCOPE ===============
tile1 = load_tiles("imgs1")
tile2 = load_tiles("imgs2")
tile3 = load_tiles("imgs3")
tile4 = load_tiles("imgs4")
layer4 = []
layer3 = []
layer2 = []
layer1 = []
g = pygame.sprite.Group()
# Load, scale and show the layers
layer4 = load_map("layer4.pkl", layer4)
layer3 = load_map("layer3.pkl", layer3)
layer2 = load_map("layer2.pkl", layer2)
layer1 = load_map("layer1.pkl", layer1)
show_map()
player = Sprite(50, 128)



# ================================= Sprite Player ====
# Clock initialization for the frame rate
clock = pygame.time.Clock()

moveLeft = False
moving_right = False
moveUp = False
moveDown = False
faceRight = False
MOVESPEED = 3
font = pygame.font.SysFont("Arial", 14)

while True:
# Check for events.

    # MOVEMENT CHECKS
    # player_movement = [0,0]
    # if moving_right == True:
    #     player_movement[0] += 1


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moving_right = False
                moveLeft = True
                faceRight = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moving_right = True
                faceRight = False
                player.image = player.list[int(player.counter)]
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
            if event.key == K_x:
                print(player.rect.x, player.rect.y)
        # KEYUP

        if event.type == KEYUP:
            player.counter = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False

# Draw the white background onto the surface.
    # display.fill((50, 75, 100))


    # Move the player.
    if moveDown and player.rect.bottom < h:
        player.rect.top += MOVESPEED
    if moveUp and player.rect.top > 0:
        player.rect.top -= MOVESPEED
    if moveLeft and player.rect.left > -35:
        player.rect.left -= MOVESPEED
        # try:
        #     player.counter += .1
        player.image = player.listflip[int(player.counter)]
        # except:
        #     player.counter = 0
            # player.image = player.listflip[int(player.counter)]
    if moving_right and player.rect.right < w + 35:
        player.rect.right += MOVESPEED
        # try:
            # player.counter -= .1
        player.image = player.list[int(player.counter)]
        # except:
        #     player.counter = 0
        #     player.image = player.list[int(player.counter)]

    
    # Draw the player onto the surface.
    # screen.fill((0, 0, 90))
    # screen.blit(display, (0,0))
    g.draw(screen)
    g.update()
    screen.blit(fps(), (10, 0))
    # Draw the window onto the screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()