import sys
import pygame.mouse
from CONSTANTS import *

pygame.init()

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Survival game")
SCREEN.blit(BACKGROUND, (0, 0))


class MainMenu(object):
    def draw_text(self, text, font, color, surface, distance):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect(center=(WIDTH/2, (HEIGHT/2)+distance))
        surface.blit(text_obj, text_rect)

    def start_game(self):
        running = True
        while running:
            SCREEN.fill((0, 0, 0))

            MainMenu().draw_text('game', pygame.font.Font(FONT_TYPE, FONT_SIZE), (255, 255, 255), SCREEN, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            CLOCK.tick(60)

    def options(self):
        running = True
        while running:
            SCREEN.fill((0, 0, 0))

            MainMenu().draw_text('options', pygame.font.Font(FONT_TYPE, FONT_SIZE), (255, 255, 255), SCREEN, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            CLOCK.tick(60)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main(self):
        button_1 = pygame.Rect(260, 155, 200, 40)
        button_2 = pygame.Rect(260, 215, 200, 40)
        button_3 = pygame.Rect(260, 275, 200, 40)

        pygame.draw.rect(SCREEN, (118, 118, 118), button_1)
        pygame.draw.rect(SCREEN, (118, 118, 118), button_2)
        pygame.draw.rect(SCREEN, (118, 118, 118), button_3)
        MainMenu().draw_text("START", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, -30)
        MainMenu().draw_text("OPTIONS", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, 30)
        MainMenu().draw_text("EXIT", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, 90)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MainMenu().terminate()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if button_1.collidepoint(mouse_pos):
                        MainMenu().start_game()

                    if button_2.collidepoint(mouse_pos):
                        MainMenu().options()

                    if button_3.collidepoint(mouse_pos):
                        MainMenu().terminate()

            pygame.display.update()
            CLOCK.tick(FPS)


if __name__ == '__main__':
    MainMenu().main()
