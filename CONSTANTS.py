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

SKELETON = [pygame.image.load(r'Sprites\SL1.png'),
            pygame.image.load(r'Sprites\SL2.png'),
            pygame.image.load(r'Sprites\SL3.png'),
            pygame.image.load(r'Sprites\SL4.png'),
            pygame.image.load(r'Sprites\SL5.png'),
            pygame.image.load(r'Sprites\SL6.png'),
            pygame.image.load(r'Sprites\SL7.png'),
            pygame.image.load(r'Sprites\SL8.png'),
            pygame.image.load(r'Sprites\SL9.png'),
            pygame.image.load(r'Sprites\SL10.png'),
            pygame.image.load(r'Sprites\SL11.png')]

CHEST = pygame.image.load(r"Sprites\chest.png")

CHEST_OPENED = pygame.image.load(r"Sprites\chest_opened.png")

X = 50
Y = 290
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 60
VEL = 5

FPS = 27
CLOCK = pygame.time.Clock()

IMAGE = r"Pictures\images.jpg"
BACKGROUND = pygame.image.load(IMAGE)
LEVEL1 = pygame.image.load(r"Pictures\level1.jpg")
WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()

BACKGROUND_X = 0
BACKGROUND_X_2 =LEVEL1.get_width()
SKELETON_LIVING = False
OPENED = False
LEFT = False
RIGHT = False
SKELETON_COUNT = 0
STAND_COUNT = 0
WALK_COUNT = 0
FONT_TYPE = r'Fonts\pixeboy.ttf'
FONT_SIZE = 60
