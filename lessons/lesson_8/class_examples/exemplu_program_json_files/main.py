# Program
# Inregistrare user +
# Vedem lista de user +
# Salveze userii in fisier +
import json


def read_users_form_file():
    try:
        file = open('users.json', 'r')
        data = file.read()
        users = json.loads(data)
    except FileNotFoundError:
        users = []
    return users


def write_users_to_file(users: list):
    file = open('users.json', 'w')
    json_string = json.dumps(users)
    file.write(json_string)
    file.close()


def list_users():
    user_list = read_users_form_file()
    if not user_list:
        print('\n No users found \n')
    for user in user_list:
        print(f"User {user['name']} age: {user['age']}")


def register_user():
    name = input('Input name')
    try:
        age = int(input('Input age'))
    except ValueError:
        print('Age set to -1')
        age = -1
    users_list = read_users_form_file()
    users_list.append({
        'name': name,
        'age': age
    })
    write_users_to_file(users_list)


def main():
    while True:
        print('\n ')
        print('Choose option: ')
        print('1. List all users. ')
        print('2. Register new user. ')
        print('3. Exit. ')
        option = input('Choose: ')
        if option == '1':
            list_users()
        elif option == '2':
            register_user()
        elif option == '3':
            exit()
        print('\n')


main()
