class Shape:

    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    def set_inner_color(self, value):
        self._inner_color = value

    def set_border_color(self, value):
        self._border_color = value

    def get_inner_color(self):
        return self._inner_color

    def get_border_color(self):
        return self._border_color
