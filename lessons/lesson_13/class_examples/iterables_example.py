class my_list:

    def __init__(self, elements=None):
        self.elements = elements or []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.elements):
            raise StopIteration()
        element = self.elements[self.index]
        self.index += 1
        return element


for a in my_list([1, 2, 3, 4, 5, 6]):
    print(a)


class Cat:

    def __init__(self, name):
        self.name = name


class CatList:

    def __init__(self, elements):
        self._elements = elements or []

    def __iter__(self):
        return iter(self._elements)

    def add_cat(self):
        pass

    def feed_cats(self):
        pass


cat_list_inst = CatList(...)

for cat in cat_list_inst:
    pass
