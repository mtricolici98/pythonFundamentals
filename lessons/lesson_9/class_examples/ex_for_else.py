def print_if_found(list_to_search, item_to_find):
    found = False
    for element in list_to_search:
        if item_to_find == element:
            print(f'Found {element} in list')
            found = True
            break
        else:
            print(f'Not found yet')
    if not found:
        print('Not found at all')


print_if_found([2, 4, 6, 8], 10)
