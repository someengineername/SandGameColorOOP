class CellClass:

    def __init__(self, type: str, movable: bool, color: tuple):
        cell_types = {'empty', 'border', 'block'}

        if type not in cell_types:
            raise Exception('Wrong cell type!')
        self._type = type
        self._movable = movable
        self._color = color

    def get_type(self):
        return self._type
