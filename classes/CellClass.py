from config import *


class CellClass:

    def __init__(self, type: str, movable: bool, color: tuple, matrix_coordinate_x=0, matrix_coordinate_y=0):
        cell_types = {'Empty', 'Border', 'Block'}

        if type not in cell_types:
            raise Exception('Wrong cell type!')
        self._type = type
        self._movable = movable
        self._color = color
        self._matrix_coordinate_x = matrix_coordinate_x
        self._matrix_coordinate_y = matrix_coordinate_y

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def is_movable(self):
        return self._movable

    def __repr__(self):
        return f'{self._type} {self._matrix_coordinate_x}-{self._matrix_coordinate_y}'

    def get_rect(self):
        return (
            cell_gap + ((cell_length + cell_gap) * self._matrix_coordinate_x),
            screen_height - cell_gap - cell_length - (
                    cell_gap + cell_length) * self._matrix_coordinate_y, cell_length, cell_length)
