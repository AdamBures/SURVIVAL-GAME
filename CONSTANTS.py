import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


WALK_RIGHT = [pygame.image.load(r'Sprites\R1.png'),
              pygame.image.load(r'Sprites\R2.png'),
              pygame.image.load(r'Sprites\R3.png'),
              pygame.image.load(r'Sprites\R4.png'),
              pygame.image.load(r'Sprites\R5.png'),
              pygame.image.load(r'Sprites\R6.png'),
              pygame.image.load(r'Sprites\R7.png'),
              pygame.image.load(r'Sprites\R8.png')]
              
WALK_LEFT = [pygame.image.load(r'Sprites\L1.png'),
             pygame.image.load(r'Sprites\L2.png'),
             pygame.image.load(r'Sprites\L3.png'),
             pygame.image.load(r'Sprites\L4.png'),
             pygame.image.load(r'Sprites\L5.png'),
             pygame.image.load(r'Sprites\L6.png'),
             pygame.image.load(r'Sprites\L7.png'),
             pygame.image.load(r'Sprites\L8.png')]

PLAYER = [pygame.image.load(r'Sprites\S1.png'),
          pygame.image.load(r'Sprites\S2.png'),
          pygame.image.load(r'Sprites\S3.png'),
          pygame.image.load(r'Sprites\S4.png'),
          pygame.image.load(r'Sprites\S5.png'),
          pygame.image.load(r'Sprites\S6.png'),
          pygame.image.load(r'Sprites\S7.png'),
          pygame.image.load(r'Sprites\S8.png')]

CHEST = pygame.image.load(r"Sprites\chest.png")

CHEST_OPENED = pygame.image.load(r"Sprites\chest_opened.png")

X = 50
Y = 290
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 60
VEL = 5

FPS = 60
CLOCK = pygame.time.Clock()

IMAGE = r"Pictures\images.jpg"
BACKGROUND = pygame.image.load(IMAGE)
LEVEL1 = pygame.image.load(r"Pictures\level1.jpg")
WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()

LEFT = False
RIGHT = False
STAND_COUNT = 0
WALK_COUNT = 0
FONT_TYPE = r'Fonts\pixeboy.ttf'
FONT_SIZE = 60
