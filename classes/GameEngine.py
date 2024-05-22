from classes.GameField import GameField
from classes.DrawingRect import DrawingRect
from config import *
import pygame
import time


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

                    mouse_coordinates = pygame.mouse.get_pos()
                    mouse_matrix_position = [mouse_coordinates[0] // (cell_length + cell_gap),
                                             (screen_height - mouse_coordinates[1]) // (cell_length + cell_gap)]
                    game_field.create_block(mouse_matrix_position[0], mouse_matrix_position[1])

                    print(mouse_coordinates, mouse_matrix_position)

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed_status = False

            # -------------
            # 2. change game variables / status
            # -------------

            game_field.update()

            if pygame.mouse.get_focused():

                mouse_coordinates = pygame.mouse.get_pos()
                mouse_matrix_position = [mouse_coordinates[0] // (cell_length + cell_gap),
                                         (screen_height - mouse_coordinates[1]) // (cell_length + cell_gap)]

                game_field.create_block(mouse_matrix_position[0], mouse_matrix_position[1])



            # TODO mouse interaction - place moving block by coordinates of a click

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

            # show white rectangle in top left when mouse button pressed and hold
            if mouse_pressed_status:
                drawing_buffer.append(DrawingRect((255, 255, 255), (50, 50, 50, 50)))

            # -------------
            #       3.2 draw each element from buffer
            # -------------
            for pos in drawing_buffer:
                pygame.draw.rect(screen, pos.get_color(), pos.get_rect())

            time.sleep(0.01)
            # print(game_field.get_status())
            pygame.display.update()

        pygame.quit()
