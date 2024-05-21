from classes.CellClass import CellClass
from config import *


class GameField:

    def __init__(self, x=gamefield_cells_x, y=gamefield_cells_y):
        self._dimension_x = x
        self._dimension_y = y
        self._objects_array = [[CellClass('empty', True, (0, 0, 0)) for j in range(self._dimension_x)] for i in
                               range(self._dimension_y)]
        print('   Field init:')
        print('   x:', self._dimension_x)
        print('   y:', self._dimension_y)
