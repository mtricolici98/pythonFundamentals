import math

from lessons.lesson_11.homework_solutions.Shape import Shape


class Circle(Shape):

    def __init__(self, radius, inner_color, border_color):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def set_radius(self, value):
        self._radius = value

    def get_radius(self):
        return self._radius

    @property
    def area(self):
        return self._radius * math.pi

    def __eq__(self, other):
        return isinstance(other, Circle) and other.area == self.area

    def __lt__(self, other):
        return isinstance(other, Circle) and other.area < self.area

    def __gt__(self, other):
        return isinstance(other, Circle) and other.area > self.area

    def __ge__(self, other):
        return isinstance(other, Circle) and other.area >= self.area

    def __le__(self, other):
        return isinstance(other, Circle) and other.area <= self.area

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other.get_radius(), self.get_inner_color(),
                          self.get_border_color())
        raise TypeError('Type is not circle')

    def __sub__(self, other):
        if isinstance(other, Circle):
            radius = self._radius - other.get_radius()
            if radius < 0:
                raise Exception('Shape sub result cant be less than 0')
            return Circle(radius, self.get_inner_color(), self.get_border_color())
        raise TypeError('Type is not circle')

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other.get_radius(), self.get_inner_color(), self.get_border_color())
        if isinstance(other, (int, float)):
            return Circle(self._radius * other, self.get_inner_color(), self.get_border_color())
        raise TypeError('Type is not rectangle')
