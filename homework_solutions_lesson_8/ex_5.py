import json


def read_dishes_from_file():
    try:
        file = open('dishes.json', 'r')
        data = file.read()
        dishes = json.loads(data)
    except FileNotFoundError:
        dishes = []
    return dishes


def write_dishes_to_file(dishes: list):
    file = open('dishes.json', 'w')
    json_string = json.dumps(dishes)
    file.write(json_string)
    file.close()


def list_dishes():
    dish_list = read_dishes_from_file()
    if not dish_list:
        print('\n No dish found \n')
    for dish in dish_list:
        print(f"Dish: {dish}")


def register_dish():
    name = input('Input name for the dish: ')
    dish_set = set(read_dishes_from_file())  # Using a set to avoid dish duplicates
    dish_set.add(name)
    write_dishes_to_file(list(dish_set))  # Sending list to save to file


def main():
    while True:
        print('\n ')
        print('Choose option: ')
        print('1. List all dishes. ')
        print('2. Register new dish. ')
        print('3. Exit. ')
        option = input('Choose: ')
        if option == '1':
            list_dishes()
        elif option == '2':
            register_dish()
        elif option == '3':
            exit()
        print('\n')


def test_ex_5():
    main()
