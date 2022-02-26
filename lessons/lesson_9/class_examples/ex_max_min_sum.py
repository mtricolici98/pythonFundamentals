print(max(1, 2, 3))
print(max([1, 2, 3]))
print(max((1, 2, 3)))
print(max({1, 2, 3}))

print(max({1: 5, 2: 6, 3: 7}))
print(max({1: 5, 2: 6, 3: 7}.values()))
print(max({1: 5, 2: 6, 3: 7}.items()))

print('_---------------------------')
for el in {1: 5, 2: 6, 3: 7}:
    print(el)
print('_---------------------------')
for el in {1: 5, 2: 6, 3: 7}.values():
    print(el)
print('_---------------------------')
for el in {1: 5, 2: 6, 3: 7}.items():
    print(el)
for key, value in {1: 5, 2: 6, 3: 7}.items():
    print(key, value)

my_dict = {1: 5, 2: 6, 3: 7}
print(max(my_dict.values()))
print(max(my_dict))

## Functia Sorted

my_list = [1, 5, 7, 4, 10, 2, 20]
my_tuple = (1, 5, 7, 4, 10, 2, 20)
my_set = {1, 5, 7, 4, 10, 2, 20}
my_dict = {1: 'value', 5: 'value', 7: 'value', 4: 'value', 10: 'value', 2: 'value', 20: 'value'}

print(sorted(my_list))
print(sorted(my_list, reverse=True))

print(sorted(my_tuple))
print(sorted(my_dict))
print(sorted(my_set))