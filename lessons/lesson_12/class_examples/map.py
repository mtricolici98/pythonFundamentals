list_of_items = ['10', '08', '2020']

int_list_of_itmes = [int(a) for a in list_of_items]
also_int_list_of_items = map(int, list_of_items)
print(int_list_of_itmes)
print(also_int_list_of_items)
