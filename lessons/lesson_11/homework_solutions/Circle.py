from lessons.lesson_11.homework_solutions.Shape import Shape


class Circle(Shape):

    def __init__(self, radius, inner_color, border_color):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def set_radius(self, value):
        self._radius = value

    def get_radius(self):
        return self._radius
