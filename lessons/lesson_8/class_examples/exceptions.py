class ListItemNotFound(Exception):
    pass


def find_index(list, item):
    index = -1
    for i in range(len(list)):
        if list[i] == item:
            return i
    raise ListItemNotFound(f'Item {item} not found in {list}')


try:
    print(find_index([1, 2, 3], 4))
except ListItemNotFound as ex:
    print('Not found')
