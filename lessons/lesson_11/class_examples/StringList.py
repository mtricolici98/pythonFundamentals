class StringList(list):

    def __init__(self, iterable):
        self._check_is_iterable_string(iterable)
        super().__init__(iterable)

    def _check_is_iterable_string(self, iterable):
        for i in iterable:
            if type(i) is not str:
                raise TypeError('Expected Strings Only')

    def append(self, __object) -> None:
        self._check_is_iterable_string([__object])
        super().append(__object)

    def extend(self, __iterable) -> None:
        self._check_is_iterable_string(__iterable)
        super().extend(__iterable)

    def total_char_count(self):
        total_count = 0
        for el in self:
            total_count += len(el)
        return total_count

    def join(self, sep=''):
        str = ''
        for el in self:
            str += el + sep
        return str


if __name__ == '__main__':
    my_str_list = StringList(['one', 'two', 'three'])
    my_str_list.append("123")
    print(my_str_list.total_char_count())
    print(my_str_list.join('; '))
    print(my_str_list)
    print(my_str_list[0])
    my_str_list[0] = 1
    print(my_str_list[0])
    print(my_str_list)
