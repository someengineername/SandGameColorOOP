from classes.GameField import GameField
from config import *
import pygame
import time


class GameEngine:
    @staticmethod
    def start_game():

        # init of pygame and game field
        pygame.init()
        game_field = GameField()

        # icon change
        new_icon = pygame.image.load('icon.png')
        pygame.display.set_icon(new_icon)
        pygame.display.set_caption('SandGameColorOOP')


        # pygame screen init
        screen = pygame.display.set_mode((screen_width, screen_height))

        # pygame flag
        run = True

        # mouse interaction variables
        mouse_pressed_status = False

        while run:

            # mouse_matrix_position = [0, 0]

            # -------------
            # 1. gather inputs
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
            # 2. change game variables / status
            # -------------

            game_field.update()

            if pygame.mouse.get_focused() and mouse_pressed_status:

                mouse_coordinates = pygame.mouse.get_pos()
                mouse_matrix_position = [mouse_coordinates[0] // (cell_length + cell_gap),
                                         (screen_height - mouse_coordinates[1]) // (cell_length + cell_gap)]

                game_field.create_block(mouse_matrix_position[0], mouse_matrix_position[1])

            # -------------
            # 3. drawing a result
            # -------------

            # filling back layer
            screen.fill(screen_base_color)

            # init of drawing buffer
            drawing_buffer = []

            # -------------
            #       3.1 filling drawing buffer with stuff (rects, in fact)
            # -------------

            # add each element from game field
            for pos in game_field.drawing_prep():
                drawing_buffer.append(pos)

            # -------------
            #       3.2 draw each element from buffer
            # -------------
            for pos in drawing_buffer:
                pygame.draw.rect(screen, pos.get_color(), pos.get_rect())

            time.sleep(0.001)
            pygame.display.update()

        pygame.quit()
