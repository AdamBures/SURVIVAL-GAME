import sys
import pygame.mouse
from pygame import mixer
import CONSTANTS
from CONSTANTS import *

# Difference between sprite position and mouse position is 67 units

pygame.init()

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Survival game")
SCREEN.blit(BACKGROUND, (0, 0))


class Player(object):
    def __init__(self):
        self.HEALTH = 3
        self.STAMINA = 5

    def check_if_dead(self):
        if self.HEALTH == 0 and not CONSTANTS.DEAD:
            CONSTANTS.DEAD = True
            print("Dead")
            return True

    def check_if_out_of_stamina(self):
        if self.STAMINA == 0 and not CONSTANTS.OUT_OF_STAMINA:
            CONSTANTS.OUT_OF_STAMINA = True
            print("Out of Stamina")
            return True

    def jump(self):
        if CONSTANTS.JUMPING:
            if CONSTANTS.JUMP_COUNT >= -10:
                CONSTANTS.Y -= (CONSTANTS.JUMP_COUNT * abs(CONSTANTS.JUMP_COUNT)) * 0.5
                CONSTANTS.JUMP_COUNT -= 1
            else:
                CONSTANTS.JUMP_COUNT = 10
                CONSTANTS.JUMPING = False


class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((13, 13, 13))
        self.image.set_colorkey((13, 13, 13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter: str, pos: pygame.sprite.Sprite):
        s = self.font.render(letter, True, (255, 255, 0))
        self.image.blit(s, pos)


class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = ''
        self.cooldown = 0
        self.cooldowns = {'.': 12,
                          '[': 18,
                          ']': 18,
                          ' ': 5,
                          '\n': 30}

    def write(self, text: str):
        self.text = list(text)

    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1


def play_song(filename: str):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(0)
    mixer.music.play(loops=-1)


def redraw_game_window():
    global back_to_menu, stop_music
    SCREEN.blit(LEVEL1, (0, 0))
    SCREEN.blit(CONSTANTS.CHEST, (WIDTH // 2, 290))
    back_to_menu = pygame.Rect(10, 10, 40, 40)
    pygame.draw.rect(SCREEN, (118, 118, 118), back_to_menu, border_radius=4)
    stop_music = pygame.Rect(150, 10, 40, 40)
    pygame.draw.rect(SCREEN, (118, 118, 118), stop_music, border_radius=4)
    MainMenu().draw_text_with_position("<-", pygame.font.Font(FONT_TYPE, 32), (255, 255, 255), SCREEN, 15, 20)
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

    elif CONSTANTS.DYING_COUNT + 1 >= 12:
        CONSTANTS.DYING_COUNT = 0

    elif CONSTANTS.HEALING_COUNT + 1 >= 24:
        CONSTANTS.HEALING_COUNT = 0
        CONSTANTS.HEALING = False

    elif CONSTANTS.SLIDE_COUNT + 1 >= 30:
        CONSTANTS.SLIDE_COUNT = 0
        CONSTANTS.SLIDING_BOOL_RIGHT = False

    elif CONSTANTS.SKELETON_ATTACK_COUNT + 1 >= 54:
        CONSTANTS.SKELETON_ATTACK_COUNT = 0

    elif CONSTANTS.ATTACK_RIGHT_COUNT + 1 >= 60:
        CONSTANTS.ATTACK_RIGHT_COUNT = 0
        CONSTANTS.ATTACK_RIGHT_BOOL = False

    elif CONSTANTS.ATTACK_LEFT_COUNT + 1 >= 60:
        CONSTANTS.ATTACK_LEFT_COUNT = 0
        CONSTANTS.ATTACK_LEFT_BOOL = False

    if CONSTANTS.OPENED:
        SCREEN.blit(CONSTANTS.CHEST_OPENED, (WIDTH // 2, 290))

    if CONSTANTS.SKELETON_LIVING:
        SCREEN.blit(pygame.transform.scale(SKELETON[CONSTANTS.SKELETON_COUNT // 3], (46, 46)), (290, 305))

    elif CONSTANTS.SKELETON_ATTACKING:
        SCREEN.blit(pygame.transform.scale(SKELETON_ATTACKING[CONSTANTS.SKELETON_ATTACK_COUNT // 3],
                                           (92, 46)), (290, 305))
        CONSTANTS.SKELETON_LIVING = False

    if CONSTANTS.LEFT:
        SCREEN.blit(pygame.transform.scale(WALK_LEFT[CONSTANTS.WALK_COUNT // 3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.WALK_COUNT += 1

    elif CONSTANTS.RIGHT:
        SCREEN.blit(pygame.transform.scale(WALK_RIGHT[CONSTANTS.WALK_COUNT // 3], (128, 64)),
                    (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.WALK_COUNT += 1

    elif CONSTANTS.CROUCHING:
        SCREEN.blit(CROUCH[CONSTANTS.CROUCH_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.CROUCH_COUNT += 1

    elif CONSTANTS.PRAYING:
        SCREEN.blit(PRAY[CONSTANTS.PRAY_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.PRAY_COUNT += 1

    elif CONSTANTS.DYING:
        try:
            SCREEN.blit(DYING[CONSTANTS.DYING_COUNT], (CONSTANTS.X, CONSTANTS.Y))
            CONSTANTS.DYING_COUNT += 1
        except IndexError:
            SCREEN.blit(pygame.transform.scale(DYING[3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))

    elif CONSTANTS.ATTACK_RIGHT_BOOL:
        try:
            SCREEN.blit(ATTACK_RIGHT[CONSTANTS.ATTACK_RIGHT_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
            CONSTANTS.ATTACK_RIGHT_COUNT += 1
        except IndexError:
            CONSTANTS.ATTACK_RIGHT_COUNT = 0
    elif CONSTANTS.ATTACK_LEFT_BOOL:
        SCREEN.blit(ATTACK_LEFT[CONSTANTS.ATTACK_LEFT_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.ATTACK_LEFT_COUNT += 1

    elif CONSTANTS.SLIDING_BOOL_RIGHT:
        SCREEN.blit(SLIDING[CONSTANTS.SLIDE_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.SLIDE_COUNT += 1

    elif CONSTANTS.SLIDING_BOOL_LEFT:
        SCREEN.blit(pygame.transform.flip(SLIDING[CONSTANTS.SLIDE_COUNT // 3], True, False), (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.SLIDE_COUNT += 1

    elif CONSTANTS.HEALING:
        SCREEN.blit(HEAL[CONSTANTS.HEALING_COUNT // 3], (CONSTANTS.X, CONSTANTS.Y))
        CONSTANTS.HEALING_COUNT += 1

    else:
        SCREEN.blit(pygame.transform.scale(PLAYER[CONSTANTS.STAND_COUNT // 3], (128, 64)), (CONSTANTS.X, CONSTANTS.Y))


class Level1(object):
    pass


def fade(width: int, height: int):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redraw_game_window()
        SCREEN.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)


class MainMenu(object):
    def __init__(self):
        super().__init__()

    def draw_text_with_position(self, text: str, font, color: tuple, surface, x: int, y: int) -> None:
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_text(self, text, font, color, surface, distance):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + distance))
        surface.blit(text_obj, text_rect)

    def start_game(self):
        play_song(CONSTANTS.SONG)
        mixer.set_num_channels(10)
        channel = mixer.Channel(0)
        running = True
        paused = False
        while running:
            redraw_game_window()
            CLOCK.tick(FPS)
            if CONSTANTS.X == 50:
                CONSTANTS.SKELETON_LIVING = True
                CONSTANTS.SKELETON_ATTACKING = False
                CONSTANTS.SKELETON_COUNT += 1
            else:
                CONSTANTS.SKELETON_ATTACKING = True
                CONSTANTS.SKELETON_LIVING = False
                CONSTANTS.SKELETON_ATTACK_COUNT += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    print(f"{CONSTANTS.X} {pygame.mouse.get_pos()}")

                    if back_to_menu.collidepoint(mouse_pos):
                        MainMenu().main()

                    elif stop_music.collidepoint(mouse_pos):
                        print("Pausing")
                        if paused:
                            paused = False
                            mixer.music.unpause()
                        elif not paused:
                            paused = True
                            mixer.music.pause()

                    if event.button == 1 and CONSTANTS.X + 67 < mouse_pos[0]:
                        CONSTANTS.ATTACK_RIGHT_BOOL = True

                    elif event.button == 1 and CONSTANTS.X + 67 > mouse_pos[0]:
                        print("Pressed")
                        CONSTANTS.ATTACK_LEFT_BOOL = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_RIGHT]:
                    CONSTANTS.X += VEL * 2
                    CONSTANTS.SLIDING_BOOL_RIGHT = True
                    CONSTANTS.SLIDING_BOOL_LEFT = False
                    CONSTANTS.SLIDE_COUNT += 1
                    print("Sliding")

                elif keys[pygame.K_LEFT] and CONSTANTS.X > CONSTANTS.VEL:
                    CONSTANTS.X -= VEL * 2
                    CONSTANTS.SLIDING_BOOL_LEFT = True
                    CONSTANTS.SLIDING_BOOL_RIGHT = False
                    CONSTANTS.SLIDE_COUNT += 1
                    print("Sliding left")

            elif keys[pygame.K_SPACE] and CONSTANTS.JUMPING is False:
                CONSTANTS.JUMPING = True

            elif CONSTANTS.JUMPING:
                CONSTANTS.Y -= CONSTANTS.VEL_Y * 4
                CONSTANTS.VEL_Y -= 1
                if CONSTANTS.VEL_Y < -10:
                    CONSTANTS.JUMPING = False
                    CONSTANTS.VEL_Y = 10

            elif keys[pygame.K_LEFT] and CONSTANTS.X > 0:
                CONSTANTS.X -= VEL
                CONSTANTS.RIGHT = False
                CONSTANTS.LEFT = True
                print("left")

            elif keys[pygame.K_RIGHT] and CONSTANTS.X < 680:
                CONSTANTS.X += VEL
                CONSTANTS.RIGHT = True
                CONSTANTS.LEFT = False
                print('right')

            elif keys[pygame.K_LCTRL]:
                CONSTANTS.CROUCHING = True

            elif Player().check_if_dead():
                CONSTANTS.DYING = True
                print("You are dead :(((")

            elif keys[pygame.K_e]:
                CONSTANTS.PRAYING = True
                print("Praying")

            elif keys[pygame.K_g]:
                sound = mixer.Sound(CONSTANTS.BONUS)
                channel.set_volume(0.2)
                channel.play(sound)
                CONSTANTS.HEALING = True
                print("Healing")

            elif keys[pygame.K_h]:
                fade(CONSTANTS.WIDTH, CONSTANTS.HEIGHT)

            elif keys[pygame.K_KP_ENTER] and CONSTANTS.X in [310, 320, 330, 340, 350] and CONSTANTS.Y == 290:
                CONSTANTS.OPENED = True
                print("Open")

            elif keys[pygame.K_ESCAPE]:
                MainMenu().main()

            elif keys[pygame.K_SPACE]:
                CONSTANTS.JUMPING = True

            else:
                CONSTANTS.DYING = False
                CONSTANTS.SLIDING_BOOL_RIGHT = False
                CONSTANTS.SLIDING_BOOL_LEFT = False
                CONSTANTS.PRAYING = False
                CONSTANTS.CROUCHING = False
                CONSTANTS.RIGHT = False
                CONSTANTS.LEFT = False
                CONSTANTS.WALK_COUNT = 0
                CONSTANTS.STAND_COUNT += 1

            pygame.display.update()

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

    def cutscene(self):
        all_sprites = pygame.sprite.Group()
        board = Board()
        cursor = Cursor(board)
        all_sprites.add(cursor, board)

        text = """
        
        
        
        
        
        
        This game is about you surviving as a knight.
        Your task is to get to treasure before orcs.
        Along the way you gotta fight them. 
        Good luck brave knight.
                                        Press Enter To Start Game!
        
        """

        cursor.write(text)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_game()

            all_sprites.update()
            SCREEN.fill((0, 0, 0))
            all_sprites.draw(SCREEN)
            pygame.display.flip()
            CLOCK.tick(60)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main(self):
        SCREEN.blit(BACKGROUND, (0, 0))
        # play_song(CONSTANTS.SONG)
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
                        self.cutscene()
                        break

                    if button_2.collidepoint(mouse_pos):
                        self.about()
                        break
                    if button_3.collidepoint(mouse_pos):
                        self.terminate()
                        break

            pygame.display.update()
            CLOCK.tick(FPS)


if __name__ == '__main__':
    MainMenu().main()
