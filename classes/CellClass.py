
class CellClass:

    def __init__(self,
                 block_type: str,
                 movable: bool = False,
                 color: tuple = None):

        cell_types = {'Empty', 'Border', 'Block'}

        if block_type not in cell_types:
            raise Exception('Wrong cell type!')

        self._type = block_type
        self._movable = movable

        self._color = (0, 0, 0)
        if color is None:
            match self._type:
                case 'Empty':
                    self._color = (100, 100, 100)
                case 'Border':
                    self._color = (255, 0, 255)
                case 'Block':
                    self._color = (255, 255, 255)
                case _:
                    self._color = (255, 0, 0)

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def is_movable(self):
        return self._movable

    def __repr__(self):
        return f'{self._type}'

    def set_movable(self, b1: bool):
        self._movable = b1
