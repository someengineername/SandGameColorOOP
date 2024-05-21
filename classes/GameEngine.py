from classes.GameField import GameField
from config import *
import pygame


class GameEngine:
    @staticmethod
    def start_game():

        # init of pygame and game field
        pygame.init()
        game_field = GameField()

        # pygame screen init
        screen = pygame.display.set_mode((screen_width, screen_height))

        # pygame flag
        run = True

        # mouse interaction variables
        mouse_pressed_status = False

        while run:

            # -------------
            # gather inputs
            # -------------

            for event in pygame.event.get():
                # window closing event
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False
                # mouse interaction event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed_status = True
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed_status = False

            # -------------
            # change game variables / status
            # -------------

            pass

            # -------------
            # drawing a result
            # -------------

            screen.fill(screen_base_color)

            if mouse_pressed_status:
                pygame.draw.rect(screen, (255, 255, 255), (50, 50, 50, 50))

            pygame.display.update()

        pygame.quit()
