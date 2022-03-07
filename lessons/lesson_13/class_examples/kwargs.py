# class Base:
#
#     def __init__(self, *args, **kwargs):
#         self.a, self.b, self.c, self.d, self.e = args
#
#
# class Derived(Base):
#
#     def __init__(self, other, another, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.other, self.another = other, another
#
#
# # Works the same way.
# example = Derived(1, 2, 3, 4, 5, 6, 7)
#
#
# ###
#
# def example(*args, **kwargs):
#     if 'one' in kwargs:
#         print('One is ', kwargs['one'])
#
#
# example(one=1, two=2, three=3)
# # Args are: (1, 2, 3)
# # Kwargs are: {'one': 1, 'two': 2, 'three': 3}
#
# dict_1 = {'one': 1, 'two': 2, 'three': 3}
#
# dict_2 = {'four': 4, **dict_1}
# print(dict_2)
#
# product = {'name': 'snikers', 'price': 10, 'sale': 0}
#
# product_sale = {**product, 'sale': 5}


def function(el):
    another_function(el)