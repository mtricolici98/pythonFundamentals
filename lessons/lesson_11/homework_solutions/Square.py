from lessons.lesson_11.homework_solutions.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_length, inner_color, border_color):
        super().__init__(side_length, side_length, inner_color, border_color)

    def set_width(self, value):
        self._width = value
        self._length = value

    def set_length(self, value):
        self._length = value
        self._width = value
