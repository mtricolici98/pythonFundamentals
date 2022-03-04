class InvalidListItemType(Exception):

    def __init__(self, type_of_element):
        self.type = type_of_element

    def __str__(self):
        return f"Invalid type of value for NumbersList, expected numeric (int or float), got {type.__name__}"


class NumbersList(list):

    def __init__(self, iterable=None):
        self._validate_is_numeric(iterable)
        super().__init__(iterable)

    def _validate_is_numeric(self, _list):
        for el in _list:
            if type(el) not in [int, float]:
                raise InvalidListItemType(type(el))

    def append(self, obj):
        self._validate_is_numeric([obj])
        super().append(obj)

    def extend(self, objs):
        self._validate_is_numeric(objs)
        super().extend(objs)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        length = len(self)
        if length == 0:
            return 0
        return self.get_sum() / length
