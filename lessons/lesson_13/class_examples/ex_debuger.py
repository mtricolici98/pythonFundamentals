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
        return isinstance(other, Rectangle) and other.area == self.area

    def __lt__(self, other):
        return isinstance(other, Rectangle) and other.area < self.area

    def __gt__(self, other):
        return isinstance(other, Rectangle) and other.area > self.area

    def __ge__(self, other):
        return isinstance(other, Rectangle) and other.area >= self.area

    def __le__(self, other):
        return isinstance(other, Rectangle) and other.area <= self.area

    def __add__(self, other):
        if not isinstance(other, Rectangle) and not issubclass(type(other), Rectangle):
            raise TypeError('Type is not rectangle')
        return Rectangle(self._width + other.get_width(), self._length + other.get_length(), self.get_inner_color(),
                         self.get_border_color())
