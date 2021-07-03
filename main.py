import sys
from CONSTANTS import *

pygame.init()

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Survival game")
SCREEN.blit(BACKGROUND, (0, 0))


FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE)
TEXT = FONT.render("SURVIVAL GAME", False, "WHITE")
TEXT_RECT = TEXT.get_rect(center=(WIDTH/2, (HEIGHT/2)-100))


def main():
    SCREEN.blit(TEXT, TEXT_RECT)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    main()
