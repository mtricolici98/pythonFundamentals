list_of_lists = [[1, 2], [2, 3], [4, 5]]

just_list = sum(list_of_lists, [])
print(just_list)

list_of_strings = ['One', 'Two', 'Three', "Four"]
my_string = ''.join(list_of_strings)
print(my_string)
print('-'.join(list_of_strings))
print('................................'.join(list_of_strings))