def find_key_with_value(some_dict, value_to_find):
    for key, value in some_dict.items():
        if value == value_to_find:
            return key


print(find_key_with_value({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'three'}, 'three'))
