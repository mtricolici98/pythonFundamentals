class Date:

    def __init__(self, day=0, month=0, year=0):
        self._day = day
        self._month = month
        self._year = year

    @property
    def full_date(self):
        return f"{self._day}-{self._month}-{self._year}"

    @full_date.setter
    def full_date(self, value):
        if Date.is_date_valid(value):
            self._day, self._month, self._year = map(int, value.split('-'))
        else:
            raise Exception('Invalid date')

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if value > 31:
            print('Invalid date')
        self._day = value

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


my_date = Date(4, 3, 2022)

my_date.day = 42
print(my_date.full_date)
# 4-3-2022
my_date.full_date = '5-4-2022'  # We use the setter for full_date to set the value
print(my_date.full_date)


class Shape:

    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    @property
    def inner_color(self):
        return self._inner_color

    @property
    def border_color(self):
        return self._border_color

    @inner_color.setter
    def inner_color(self, value):
        self._inner_color = value

    @border_color.setter
    def border_color(self, value):
        self._border_color = value


shape = Shape('green', 'black')
shape.border_color = 'white'
shape.inner_color = 'blue'

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

shape = Shape('green', 'black')
shape.get_border_color()
