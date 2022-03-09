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

    def __add__(self, other):
        if isinstance(other, Square) or issubclass(type(other), Square):
            return Square(self._width + other.get_width(), self.get_inner_color(),
                          self.get_border_color())
        raise TypeError('Type is not rectangle')

    def __sub__(self, other):
        if not isinstance(other, Square) and not issubclass(type(other), Square):
            raise TypeError('Type is not rectangle')
        width = self._width - other.get_width()
        if width < 0:
            raise Exception('Shape sub result cant be less than 0')
        return Square(self._width + other.get_width(), self.get_inner_color(),
                      self.get_border_color())

    def __mul__(self, other):
        if not isinstance(other, Square) and not issubclass(type(other), Square):
            if not isinstance(other, (int, float)):
                raise TypeError('Type is not rectangle')
        if isinstance(other, (int, float)):
            return Square(self._width * other, self.get_inner_color(), self.get_border_color())
        return Square(self._width * other.get_width(), self.get_inner_color(),
                      self.get_border_color())
