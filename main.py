import sys
from CONSTANTS import *

pygame.init()

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Survival game")
SCREEN.blit(BACKGROUND, (0, 0))


def draw_text(text, font, color, surface, distance):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect(center=(WIDTH/2, (HEIGHT/2)+distance))
    surface.blit(text_obj, text_rect)


def main():
    draw_text("START", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, -30)
    draw_text("OPTIONS", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, 30)
    draw_text("EXIT", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, 80)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    main()
