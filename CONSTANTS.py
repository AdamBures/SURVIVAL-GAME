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
              pygame.image.load(r'Sprites\R8.png'),
              pygame.image.load(r'Sprites\R9.png')]

WALK_LEFT = [pygame.image.load(r'Sprites\L1.png'),
             pygame.image.load(r'Sprites\L2.png'),
             pygame.image.load(r'Sprites\L3.png'),
             pygame.image.load(r'Sprites\L4.png'),
             pygame.image.load(r'Sprites\L5.png'),
             pygame.image.load(r'Sprites\L6.png'),
             pygame.image.load(r'Sprites\L7.png'),
             pygame.image.load(r'Sprites\L8.png'),
             pygame.image.load(r'Sprites\L9.png')]

PLAYER = pygame.image.load(r'Sprites\standing.png')

X = 50
Y = 50
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


FONT_TYPE = r'Fonts\pixeboy.ttf'
FONT_SIZE = 60
