import hashlib
import json


def register_users(nr_of_users):
    user_list = []
    for t in range(nr_of_users):
        username = input('Input username')
        password = input('Input password')
        password = hashlib.md5(password.encode()).hexdigest()  # Hashing password (never store plaintext password)
        user_list.append(
            {
                'username': username,
                'password': str(password)
            }
        )
    return user_list


def save_users_to_file(user_list):
    existing_users = dict()
    try:
        with open('users.json', 'r') as usr_file:
            users_in_file = json.loads(usr_file.read())
            for user in users_in_file:
                existing_users[user['username']] = user  # Getting all users from the file
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    for user in user_list:
        if user['username'] in existing_users:
            print(f'User {user["username"]} will be overridden')
        existing_users[user['username']] = user
    with open('users.json', 'w') as usr_file:
        usr_json = json.dumps(list(existing_users.values()))
        usr_file.write(usr_json)


def list_users_from_file():
    try:
        with open('users.json', 'r') as usr_file:
            users_in_file = json.loads(usr_file.read())
            for user in users_in_file:
                print(user)
    except FileNotFoundError as ex:
        print('No users yet')
    except Exception as ex:
        print(str(ex))


def add_users():
    nr_of_user = int(input('How many users you want to add ? '))
    users = register_users(nr_of_user)
    save_users_to_file(users)


def main():
    while True:
        print('\nSelect what you want to do ?')
        print('1 To list all users')
        print('2 To add users')
        print('3 To exit')
        ex_map = {
            1: list_users_from_file,
            2: add_users,
            3: exit
        }
        choice = int(input('Choice ?: '))
        print('\n')
        ex_map[choice]()


if __name__ == '__main__':
    main()
