import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

X = 50
Y = 50
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 60
VEL = 5

FPS = 60
CLOCK = pygame.time.Clock()

IMAGE = r"Pictures\images.jpg"
BACKGROUND = pygame.image.load(IMAGE)
WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()


FONT_TYPE = r'Fonts\pixeboy.ttf'
FONT_SIZE = 60
