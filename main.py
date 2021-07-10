import sys
import pygame.mouse
import CONSTANTS
from CONSTANTS import *

pygame.init()

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Survival game")
SCREEN.blit(BACKGROUND, (0, 0))


class Player:
    def __init__(self):
        self.left = False
        self.right = False
        self.walk_count = 0

    def redraw_game_window(self):
        SCREEN.blit(LEVEL1, (0, 0))
        if self.walk_count + 1 >= 24:
            self.walk_count = 0

        if self.left:
            SCREEN.blit(WALK_LEFT[self.walk_count // 3].convert_alpha(), (CONSTANTS.X, CONSTANTS.Y))
            self.walk_count += 1

        elif self.right:
            SCREEN.blit(WALK_RIGHT[self.walk_count // 3].convert_alpha(), (CONSTANTS.X, CONSTANTS.Y))
            self.walk_count += 1
        else:
            SCREEN.blit(PLAYER.convert_alpha(), (CONSTANTS.X, CONSTANTS.Y))
            self.walk_count = 0


def redrawGameWindow():
    SCREEN.blit(LEVEL1, (0, 0))
    SCREEN.blit(CONSTANTS.CHEST, (WIDTH//2, 290))
    MainMenu().draw_text('TUTORIAL', pygame.font.Font(FONT_TYPE, FONT_SIZE), (255, 255, 255), SCREEN, 0)
    if CONSTANTS.WALK_COUNT + 1 >= 24:
        CONSTANTS.WALK_COUNT = 0

    elif CONSTANTS.STAND_COUNT + 1 >= 24:
        CONSTANTS.STAND_COUNT = 0

    elif CONSTANTS.SKELETON_COUNT + 1 >= 24:
        CONSTANTS.SKELETON_COUNT = 0

    if CONSTANTS.OPENED:
        SCREEN.blit(CONSTANTS.CHEST_OPENED, (WIDTH//2, 290))

    if CONSTANTS.SKELETON_LIVING:
        SCREEN.blit(pygame.transform.scale(SKELETON[CONSTANTS.SKELETON_COUNT//3], (46, 46)), (290, 305))

    if CONSTANTS.LEFT:
        SCREEN.blit(pygame.transform.scale(WALK_LEFT[CONSTANTS.WALK_COUNT//3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.WALK_COUNT += 1

    elif CONSTANTS.RIGHT:
        SCREEN.blit(pygame.transform.scale(WALK_RIGHT[CONSTANTS.WALK_COUNT//3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.WALK_COUNT += 1

    else:
        SCREEN.blit(pygame.transform.scale(PLAYER[CONSTANTS.STAND_COUNT//3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))

    pygame.display.update()


class Level1(object):
    pass


class MainMenu(object):
    def __init__(self):
        super().__init__()

    def draw_text_with_position(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_text(self, text, font, color, surface, distance):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + distance))
        surface.blit(text_obj, text_rect)

    def start_game(self):
        running = True
        while running:
            CLOCK.tick(27)
            CONSTANTS.SKELETON_LIVING = True
            CONSTANTS.SKELETON_COUNT += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and CONSTANTS.X > CONSTANTS.VEL:
                CONSTANTS.X -= VEL
                CONSTANTS.RIGHT = False
                CONSTANTS.LEFT = True
                print("left")

            elif keys[pygame.K_RIGHT]:
                CONSTANTS.X += VEL
                CONSTANTS.RIGHT = True
                CONSTANTS.LEFT = False
                print('right')

            elif keys[pygame.K_e] and CONSTANTS.PLAYER[CONSTANTS.STAND_COUNT//3].get_rect().colliderect(CONSTANTS.CHEST.get_rect()):
                CONSTANTS.OPENED = True
                print("Open")

            else:
                CONSTANTS.RIGHT = False
                CONSTANTS.LEFT = False
                CONSTANTS.WALK_COUNT = 0
                CONSTANTS.STAND_COUNT += 1



            redrawGameWindow()

    def about(self):
        SCREEN.blit(BACKGROUND, (0, 0))

        back_to_menu = pygame.Rect(0, 0, 40, 40)
        pygame.draw.rect(SCREEN, (118, 118, 118), back_to_menu, border_radius=4)

        MainMenu().draw_text_with_position("<-", pygame.font.Font(FONT_TYPE, 32), (255, 255, 255), SCREEN, 5, 10)
        MainMenu().draw_text('About', pygame.font.Font(FONT_TYPE, 64), (255, 255, 255), SCREEN, -30)
        MainMenu().draw_text("This game is about you surviving as a knight.",
                             pygame.font.Font(FONT_TYPE, 24), (0, 0, 0), SCREEN, 30)
        MainMenu().draw_text("Your task is to get to treasure before orcs.",
                             pygame.font.Font(FONT_TYPE, 24), (0, 0, 0), SCREEN, 60)
        MainMenu().draw_text("Along the way you gotta fight them.",
                             pygame.font.Font(FONT_TYPE, 24), (0, 0, 0), SCREEN, 90)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if back_to_menu.collidepoint(mouse_pos):
                        MainMenu().main()

            pygame.display.update()
            CLOCK.tick(60)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main(self):
        SCREEN.blit(BACKGROUND, (0, 0))

        button_1 = pygame.Rect(260, 155, 200, 40)
        button_2 = pygame.Rect(260, 215, 200, 40)
        button_3 = pygame.Rect(260, 275, 200, 40)

        pygame.draw.rect(SCREEN, (118, 118, 118), button_1, border_radius=4)
        pygame.draw.rect(SCREEN, (118, 118, 118), button_2, border_radius=4)
        pygame.draw.rect(SCREEN, (118, 118, 118), button_3, border_radius=4)
        MainMenu().draw_text("START", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, -30)
        MainMenu().draw_text("ABOUT", pygame.font.Font(FONT_TYPE, FONT_SIZE), "WHITE", SCREEN, 30)
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
                        break

                    if button_2.collidepoint(mouse_pos):
                        MainMenu().about()
                        break
                    if button_3.collidepoint(mouse_pos):
                        MainMenu().terminate()
                        break
            pygame.display.update()
            CLOCK.tick(FPS)


if __name__ == '__main__':
    MainMenu().main()
