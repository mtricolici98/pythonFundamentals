nr_of_users = int(input('How many users you want to register?: '))
users_list = []
for _ in range(nr_of_users):
    first_name = input('First name:')
    last_name = input('Last name:')
    age = int(input('Age:'))
    prof = input('Profession:')
    if age < 14:
        print(f'{first_name} {last_name} can\'t be registered because they are under 14 years')
    else:
        users_list.append(
            dict(
                first_name=first_name,
                last_name=last_name,
                age=age,
                profession=prof
            )
        )
        print(f'Registration for the {prof} {first_name} {last_name} aged {age} is complete.')

# Storing a dict where min age and max age are the key as a tuple
between_14_18 = dict(min=14, max=18, list=[])
between_19_25 = dict(min=19, max=25, list=[])
between_26_45 = dict(min=26, max=45, list=[])
above_46 = dict(min=46, max=None, list=[])
for user in users_list:
    if user['age'] > 45:
        above_46['list'].append(user)
    elif user['age'] > 25:
        between_26_45['list'].append(user)
    elif user['age'] > 18:
        between_19_25['list'].append(user)
    else:
        between_14_18['list'].append(user)

user_groups = [between_19_25, between_14_18, between_26_45, above_46]

for user_group in user_groups:
    min_age, max_age = user_group['min'], user_group['max']
    if user_group['list']:  # If no users, we don't need to print
        # Again handling all combinations of min_age and max_age
        if min_age and max_age:
            print(f'Users between {min_age} and {max_age} are:')
        elif min_age:
            print(f'Users above {min_age} are:')
        elif max_age:
            print(f'Users below {max_age} are:')
        for user in user_group['list']:
            print(f"{user['first_name']} {user['last_name']}")
