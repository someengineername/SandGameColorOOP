class DrawingRect:

    def __init__(self, color=tuple, rect=tuple):
        self._color = color
        self._rect = rect

    def get_color(self):
        return self._color

    def get_rect(self):
        return self._rect
