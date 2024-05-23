from classes.CellClass import CellClass
from classes.DrawingRect import DrawingRect
import random
from config import *


class GameField:

    def __init__(self):
        self._dimension_x = gamefield_cells_x
        self._dimension_y = gamefield_cells_y
        self._gamefield_dict = dict()
        self._color = [255, 0, 0]
        self._speed = 1

        self.field_filling_default_data()

    def field_filling_default_data(self):
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
                                                          movable=True, )
                                                )

    def drawing_prep(self):
        return [DrawingRect(j.get_color(), (cell_gap + ((cell_length + cell_gap) * i[0]),
                                            screen_height - cell_gap - cell_length - (
                                                    cell_gap + cell_length) * i[1],
                                            cell_length, cell_length)) for i, j in self._gamefield_dict.items() if
                not j.get_type() == 'Border']

    def update(self):
        # go through list of movable objects and apply actions for them:

        for cell_coor, cell_object in {k: v for k, v in self._gamefield_dict.items() if
                                       v.get_type() == 'Block' and v.is_movable()}.items():

            coor_x = cell_coor[0]
            coor_y = cell_coor[1]

            bottom_cell = self._gamefield_dict[(coor_x, coor_y - 1)]
            bottom_left_cell = self._gamefield_dict[(coor_x - 1, coor_y - 1)]
            bottom_right_cell = self._gamefield_dict[(coor_x + 1, coor_y - 1)]

            # if everything's not movable - stop moving
            if not bottom_left_cell.get_type() == 'Empty' and not bottom_right_cell.get_type() == 'Empty' and not bottom_cell.get_type() == 'Empty':
                self._gamefield_dict[cell_coor].set_movable(False)
            # if left open - drop left
            elif not bottom_cell.get_type() == 'Empty' and not bottom_right_cell.get_type() == 'Empty':
                self.drop_left(coor_x, coor_y)
            # if right open - right drop
            elif not bottom_cell.get_type() == 'Empty' and not bottom_left_cell.get_type() == 'Empty':
                self.drop_right(coor_x, coor_y)
            elif not bottom_cell.get_type() == 'Empty' and bottom_left_cell.is_movable() and bottom_right_cell.get_type() == 'Empty':
                self.drop_split_chances(coor_x, coor_y)
            # if center bottom open - drop into it
            elif bottom_cell.get_type() == 'Empty':
                self.swap_places(coor_x, coor_y)

    def swap_places(self, coor_x, coor_y):
        self._gamefield_dict[(coor_x, coor_y - 1)], self._gamefield_dict[(coor_x, coor_y)] \
            = self._gamefield_dict[(coor_x, coor_y)], self._gamefield_dict[(coor_x, coor_y - 1)]

    def drop_left(self, coor_x, coor_y):
        self._gamefield_dict[(coor_x, coor_y)], self._gamefield_dict[(coor_x - 1, coor_y)] \
            = self._gamefield_dict[(coor_x - 1, coor_y)], self._gamefield_dict[(coor_x, coor_y)]

    def drop_right(self, coor_x, coor_y):
        self._gamefield_dict[(coor_x, coor_y)], self._gamefield_dict[(coor_x + 1, coor_y)] \
            = self._gamefield_dict[(coor_x + 1, coor_y)], self._gamefield_dict[(coor_x, coor_y)]

    def drop_split_chances(self, coor_x, coor_y):

        if random.randint(0, 1) == 1:
            self.drop_left(coor_x, coor_y)
        else:
            self.drop_right(coor_x, coor_y)

    def get_status(self):
        return f'Field check: {self._dimension_x * self._dimension_x == len(self._gamefield_dict)}'

    def create_block(self, coor_x, coor_y):

        points_count = random.randint(1, 2)
        new_color = self.get_color_cycle()
        for i in range(points_count):

            try:
                coor_x = random.randint(- 6, + 6) + coor_x
                coor_y = random.randint(- 6, + 6) + coor_y

                if self._gamefield_dict[(coor_x,coor_y)].is_movable():

                    self._gamefield_dict[(coor_x, coor_y)] = CellClass(block_type='Block', color=new_color,
                                                                   movable=True)
            except:
                pass

    def get_color_cycle(self):

        if self._color[0] == 255 and 255 > self._color[1] >= 0 and self._color[2] == 0:
            self._color[1] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif 0 < self._color[0] <= 255 and self._color[1] == 255 and self._color[2] == 0:
            self._color[0] -= self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 0 and self._color[1] == 255 and 255 > self._color[2] >= 0:
            self._color[2] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 0 and 0 < self._color[1] <= 255 and self._color[2] == 255:
            self._color[1] -= self._speed
            return self._color[0], self._color[1], self._color[2]

        elif 0 <= self._color[0] < 255 and self._color[1] == 0 and self._color[2] == 255:
            self._color[0] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 255 and self._color[1] == 0 and 0 <= self._color[2] <= 255:
            self._color[2] -= self._speed
            return self._color[0], self._color[1], self._color[2]
