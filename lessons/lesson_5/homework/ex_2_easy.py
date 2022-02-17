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
between_14_18 = []
between_19_25 = []
between_26_45 = []
above_46 = []
for user in users_list:
    if user['age'] > 45:
        above_46.append(user)
    elif user['age'] > 25:
        between_26_45.append(user)
    elif user['age'] > 18:
        between_19_25.append(user)
    else:
        between_14_18.append(user)

print(f'Users between 14 and 18 are:')
for user in between_14_18:
    print(f"{user['first_name']} {user['last_name']}")
print(f'Users between 19 and 25 are:')
for user in between_19_25:
    print(f"{user['first_name']} {user['last_name']}")
print(f'Users between 26 and 45 are:')
for user in between_26_45:
    print(f"{user['first_name']} {user['last_name']}")
print(f'Users above 46 are:')
for user in above_46:
    print(f"{user['first_name']} {user['last_name']}")
