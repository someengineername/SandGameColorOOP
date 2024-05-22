from classes.CellClass import CellClass
from classes.DrawingRect import DrawingRect
from config import *


class GameField:

    def __init__(self):
        self._dimension_x = gamefield_cells_x
        self._dimension_y = gamefield_cells_y
        self._objects_array = []

        self._gamefield_dict = dict()

        for i in range(self._dimension_x):
            self._gamefield_dict.setdefault((i, 0),
                                            CellClass('Border', False))

        for i in range(self._dimension_x):
            self._gamefield_dict.setdefault((i, self._dimension_y - 1),
                                            CellClass('Border', False))

        for j in range(1, self._dimension_y - 1):
            self._gamefield_dict.setdefault((0, j),
                                            CellClass('Border', False))

        for j in range(1, self._dimension_y - 1):
            self._gamefield_dict.setdefault((self._dimension_x - 1, j),
                                            CellClass('Border', False))

        for j in range(1, self._dimension_y - 1):
            for i in range(1, self._dimension_x - 1):
                self._gamefield_dict.setdefault((i, j),
                                                CellClass(block_type='Empty',
                                                          movable=False,)
                                                )

        print('Field check:', self._dimension_x * self._dimension_x == len(self._gamefield_dict))

    def drawing_prep(self):
        test_list = [DrawingRect(j.get_color(), (cell_gap + ((cell_length + cell_gap) * i[0]),
                                                 screen_height - cell_gap - cell_length - (
                                                         cell_gap + cell_length) * i[1],
                                                 cell_length, cell_length)) for i, j in self._gamefield_dict.items()]
        return test_list

    # TODO tick field update

    # def update(self):
    #
    #     go through list of movable objects and apply actions for them:
    # for pos in filter(lambda x: x.is_movable(), self._objects_array):
    #     pass

    # TODO swap places in case of straight falling
    def swap_places(self):
        return False

    # TODO droppping section!!!
    def drop_left(self):
        return False

    def drop_right(self):
        return False

    def drop_split_chances(self):
        return False

    def get_status_gamefield(self):
        return self._gamefield_dict
