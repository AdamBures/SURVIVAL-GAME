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

CROUCH = [pygame.image.load(r'Sprites\C1.png'),
          pygame.image.load(r'Sprites\C2.png'),
          pygame.image.load(r'Sprites\C3.png'),
          pygame.image.load(r'Sprites\C4.png'),
          pygame.image.load(r'Sprites\C5.png'),
          pygame.image.load(r'Sprites\C6.png'),
          pygame.image.load(r'Sprites\C7.png'),
          pygame.image.load(r'Sprites\C8.png')]

PRAY = [pygame.image.load(r'Sprites\P0.png'),
        pygame.image.load(r'Sprites\P1.png'),
        pygame.image.load(r'Sprites\P2.png'),
        pygame.image.load(r'Sprites\P3.png'),
        pygame.image.load(r'Sprites\P4.png'),
        pygame.image.load(r'Sprites\P5.png'),
        pygame.image.load(r'Sprites\P6.png'),
        pygame.image.load(r'Sprites\P7.png'),
        pygame.image.load(r'Sprites\P8.png'),
        pygame.image.load(r'Sprites\P9.png'),
        pygame.image.load(r'Sprites\P10.png'),
        pygame.image.load(r'Sprites\P11.png')]

ATTACK_RIGHT = [pygame.image.load(r'Sprites\ATTACK KNIGHT\R1.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R2.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R3.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R4.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R5.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R6.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R7.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R8.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R9.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R10.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R11.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R12.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R13.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R14.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R15.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R16.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R17.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R18.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R19.png'),
                pygame.image.load(r'Sprites\ATTACK KNIGHT\R20.png')]


ATTACK_LEFT = [pygame.image.load(r'Sprites\ATTACK KNIGHT\L1.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L2.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L3.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L4.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L5.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L6.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L7.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L8.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L9.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L10.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L11.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L12.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L13.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L14.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L15.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L16.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L17.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L18.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L19.png'),
               pygame.image.load(r'Sprites\ATTACK KNIGHT\L20.png')]

SLIDING = [pygame.image.load(r"Sprites\SLIDING1.png"),
           pygame.image.load(r"Sprites\SLIDING2.png"),
           pygame.image.load(r"Sprites\SLIDING3.png"),
           pygame.image.load(r"Sprites\SLIDING4.png"),
           pygame.image.load(r"Sprites\SLIDING5.png"),
           pygame.image.load(r"Sprites\SLIDING6.png"),
           pygame.image.load(r"Sprites\SLIDING7.png"),
           pygame.image.load(r"Sprites\SLIDING8.png"),
           pygame.image.load(r"Sprites\SLIDING9.png"),
           pygame.image.load(r"Sprites\SLIDING10.png")]

DYING = [pygame.image.load(r"Sprites\D1.png"),
         pygame.image.load(r"Sprites\D2.png"),
         pygame.image.load(r"Sprites\D3.png"),
         pygame.image.load(r"Sprites\D4.png")]

SKELETON_ATTACKING = [pygame.image.load(r"Sprites\SKELETON ATTACKING\tile000.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile001.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile002.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile003.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile004.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile005.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile006.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile007.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile008.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile009.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile010.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile011.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile012.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile013.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile014.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile015.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile016.png"),
                      pygame.image.load(r"Sprites\SKELETON ATTACKING\tile017.png")]

HEAL = [pygame.image.load(r"Sprites\H1.png"),
        pygame.image.load(r"Sprites\H2.png"),
        pygame.image.load(r"Sprites\H3.png"),
        pygame.image.load(r"Sprites\H4.png"),
        pygame.image.load(r"Sprites\H5.png"),
        pygame.image.load(r"Sprites\H6.png"),
        pygame.image.load(r"Sprites\H7.png"),
        pygame.image.load(r"Sprites\H8.png")]

CHEST = pygame.image.load(r"Sprites\chest.png")

CHEST_OPENED = pygame.image.load(r"Sprites\chest_opened.png")

X = 50
Y = 290
VEL_Y = 10
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 60
VEL = 5
FPS = 27
CLOCK = pygame.time.Clock()

SONG = r"Songs\theme.mp3"
CRUSH = r"Effects\bone crush.mp3"
BONUS = r"Effects\bonus.wav"
CLICK = r"Effects\click.wav"
HEALING_SOUND = r"Effects\healing.wav"
HIT = r"Effects\hit.wav"
SWORD = r"Effects\sword.mp3"

IMAGE = r"Pictures\images.jpg"
BACKGROUND = pygame.image.load(IMAGE)
LEVEL1 = pygame.image.load(r"Pictures\level.jpg")
WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()

BACKGROUND_X = 0
BACKGROUND_X_2 = LEVEL1.get_width()

SKELETON_LIVING = False
OPENED = False
LEFT = False
RIGHT = False
PRAYING = False
ATTACK_RIGHT_BOOL = False
ATTACK_LEFT_BOOL = False
CROUCHING = False
SLIDING_BOOL_RIGHT = False
SLIDING_BOOL_LEFT = False
DEAD = False
OUT_OF_STAMINA = False
HEALING = False
JUMPING = False

HEALING_COUNT = 0
SKELETON_ATTACK_COUNT = 0
SLIDE_COUNT = 0
CROUCH_COUNT = 0
DYING_COUNT = 0
PRAY_COUNT = 0
SKELETON_COUNT = 0
STAND_COUNT = 0
WALK_COUNT = 0
ATTACK_RIGHT_COUNT = 0
ATTACK_LEFT_COUNT = 0
JUMP_COUNT = 0

FONT_TYPE = r'Fonts\pixeboy.ttf'
FONT_SIZE = 60
