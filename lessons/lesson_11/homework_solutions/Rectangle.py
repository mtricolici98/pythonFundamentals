from lessons.lesson_11.homework_solutions.Shape import Shape


class Rectangle(Shape):

    def __init__(self, width, length, inner_color, border_color):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def set_width(self, value):
        self._width = value

    def set_length(self, value):
        self._length = value

    def get_width(self):
        return self._width

    def get_length(self):
        return self._length
