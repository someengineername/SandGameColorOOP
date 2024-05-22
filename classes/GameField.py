from classes.CellClass import CellClass
from config import *


class GameField:

    def __init__(self):
        self._dimension_x = gamefield_cells_x
        self._dimension_y = gamefield_cells_y
        self._border_bot = [
            CellClass(type='Border',
                      movable=False,
                      color=(255, 0, 255),
                      matrix_coordinate_x=i,
                      matrix_coordinate_y=0) for i in range(self._dimension_x)]
        self._border_top = [
            CellClass(type='Border',
                      movable=False,
                      color=(255, 0, 255),
                      matrix_coordinate_x=i,
                      matrix_coordinate_y=self._dimension_y - 1) for i in range(self._dimension_x)]
        self._border_left = [
            CellClass(type='Border',
                      movable=False,
                      color=(255, 255, 0),
                      matrix_coordinate_x=0,
                      matrix_coordinate_y=i) for i in range(1, self._dimension_y - 1)]
        self._border_right = [
            CellClass(type='Border',
                      movable=False,
                      color=(255, 255, 0),
                      matrix_coordinate_x=self._dimension_x - 1,
                      matrix_coordinate_y=i) for i in range(1, self._dimension_y - 1)]
        self._inner_space = []

        for i in range(1, self._dimension_x - 1):
            for j in range(1, self._dimension_y - 1):
                self._inner_space.append(CellClass(type='Empty',
                                                   movable=False,
                                                   color=(50, 50, 50),
                                                   matrix_coordinate_x=i,
                                                   matrix_coordinate_y=j))

        self._objects_array = self._border_bot + self._border_top + self._border_left + self._border_right + self._inner_space

        # print(len(self._objects_array))
        print(gamefield_cells_y * gamefield_cells_x == len(self._objects_array))


    def drawing_prep(self):
        return self._objects_array


    # TODO tick field update
