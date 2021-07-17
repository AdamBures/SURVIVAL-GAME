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


def redraw_game_window():
    SCREEN.blit(LEVEL1, (0, 0))
    SCREEN.blit(CONSTANTS.CHEST, (WIDTH//2, 290))
    MainMenu().draw_text('TUTORIAL', pygame.font.Font(FONT_TYPE, FONT_SIZE), (255, 255, 255), SCREEN, 0)

    if CONSTANTS.WALK_COUNT + 1 >= 24:
        CONSTANTS.WALK_COUNT = 0

    elif CONSTANTS.STAND_COUNT + 1 >= 24:
        CONSTANTS.STAND_COUNT = 0

    elif CONSTANTS.SKELETON_COUNT + 1 >= 24:
        CONSTANTS.SKELETON_COUNT = 0

    elif CONSTANTS.CROUCH_COUNT + 1 >= 24:
        CONSTANTS.CROUCH_COUNT = 0

    elif CONSTANTS.PRAY_COUNT + 1 >= 36:
        CONSTANTS.PRAY_COUNT = 0

    elif CONSTANTS.SLIDE_COUNT + 1 >= 30:
        CONSTANTS.SLIDE_COUNT = 0
        CONSTANTS.SLIDING_BOOL = False

    elif CONSTANTS.ATTACK_RIGHT_COUNT + 1 >= 60:
        CONSTANTS.ATTACK_RIGHT_COUNT = 0
        CONSTANTS.ATTACK_RIGHT_BOOL = False

    elif CONSTANTS.ATTACK_LEFT_COUNT + 1 >= 60:
        CONSTANTS.ATTACK_LEFT_COUNT = 0
        CONSTANTS.ATTACK_LEFT_BOOL = False

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

    elif CONSTANTS.CROUCHING:
        SCREEN.blit(CROUCH[CONSTANTS.CROUCH_COUNT//3], (CONSTANTS.X, CONSTANTS.Y))

    elif CONSTANTS.PRAYING:
        SCREEN.blit(PRAY[CONSTANTS.PRAY_COUNT//3], (CONSTANTS.X, CONSTANTS.Y))

    elif CONSTANTS.ATTACK_RIGHT_BOOL:
        SCREEN.blit(ATTACK_RIGHT[CONSTANTS.ATTACK_RIGHT_COUNT//3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.ATTACK_RIGHT_COUNT += 1

    elif CONSTANTS.ATTACK_LEFT_BOOL:
        SCREEN.blit(ATTACK_LEFT[CONSTANTS.ATTACK_LEFT_COUNT//3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.ATTACK_LEFT_COUNT += 1

    elif CONSTANTS.SLIDING_BOOL:
        SCREEN.blit(SLIDING[CONSTANTS.SLIDE_COUNT//3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.SLIDE_COUNT += 1

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        CONSTANTS.ATTACK_RIGHT_BOOL = True

                    elif event.button == 3:
                        print("Pressed")
                        CONSTANTS.ATTACK_LEFT_BOOL = True

            keys = pygame.key.get_pressed()
            # print(CONSTANTS.WIDTH//2, CONSTANTS.X, CONSTANTS.Y)
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

            elif keys[pygame.K_LCTRL]:
                CONSTANTS.CROUCHING = True
                CONSTANTS.CROUCH_COUNT += 1

            elif keys[pygame.K_e]:
                CONSTANTS.PRAYING = True
                CONSTANTS.PRAY_COUNT += 1
                print("Praying")

            elif keys[pygame.K_KP_ENTER] and CONSTANTS.X in [310, 320, 330, 340, 350] and CONSTANTS.Y == 290:
                CONSTANTS.OPENED = True
                print("Open")

            elif keys[pygame.K_LSHIFT]:
                CONSTANTS.X += VEL*2
                CONSTANTS.SLIDING_BOOL = True
                CONSTANTS.SLIDE_COUNT += 1
                print("Sliding")

            elif keys[pygame.K_ESCAPE]:
                MainMenu().main()

            else:
                CONSTANTS.SLIDING_BOOL = False
                CONSTANTS.PRAYING = False
                CONSTANTS.CROUCHING = False
                CONSTANTS.RIGHT = False
                CONSTANTS.LEFT = False
                CONSTANTS.WALK_COUNT = 0
                CONSTANTS.STAND_COUNT += 1

            redraw_game_window()

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
