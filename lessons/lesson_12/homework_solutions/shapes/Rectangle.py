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

    @property
    def area(self):
        return self._width * self._length

    def __eq__(self, other):
        return issubclass(type(other), Rectangle) and other.area == self.area

    def __lt__(self, other):
        return issubclass(type(other), Rectangle) and other.area < self.area

    def __gt__(self, other):
        return issubclass(type(other), Rectangle) and other.area > self.area

    def __ge__(self, other):
        return issubclass(type(other), Rectangle) and other.area >= self.area

    def __le__(self, other):
        return issubclass(type(other), Rectangle) and other.area <= self.area

    def __add__(self, other):
        if isinstance(other, Rectangle) or issubclass(type(other), Rectangle):
            return Rectangle(self._width + other.get_width(), self._length + other.get_length(), self.get_inner_color(),
                             self.get_border_color())
        raise TypeError('Type is not rectangle')

    def __sub__(self, other):
        if not isinstance(other, Rectangle) and not issubclass(type(other), Rectangle):
            raise TypeError('Type is not rectangle')
        width, length = self._width - other.get_width(), self._length - other.get_length()
        if min(width, length) < 0:
            raise Exception('Shape sub result cant be less than 0')
        return Rectangle(self._width + other.get_width(), self._length + other.get_length(), self.get_inner_color(),
                         self.get_border_color())

    def __mul__(self, other):
        if not isinstance(other, Rectangle) and not issubclass(type(other), Rectangle):
            if not isinstance(other, (int, float)):
                raise TypeError('Type is not rectangle')
        if isinstance(other, (int, float)):
            return Rectangle(self._width * other, self._length * other, self.get_inner_color(), self.get_border_color())
        return Rectangle(self._width * other.get_width(), self._length * self.get_length(), self.get_inner_color(),
                         self.get_border_color())
