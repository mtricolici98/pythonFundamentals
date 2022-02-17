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
aged_dict = {
    (14, 18): [],
    (19, 25): [],
    (26, 45): [],
    (46, None): [],
}

for age_limits in aged_dict:
    min_age, max_age = age_limits  # Unpacking the tuple
    for user in users_list:
        # Handling each combination of min and max value (If no max and no min age provided we don't care)
        if max_age and min_age:
            if min_age <= user['age'] <= max_age:
                aged_dict[age_limits].append(user)
        elif min_age:
            if user['age'] >= min_age:
                aged_dict[age_limits].append(user)
        elif max_age:
            if user['age'] <= max_age:
                aged_dict[age_limits].append(user)

for age_limits, users in aged_dict.items():
    min_age, max_age = age_limits  # Unpacking the tuple
    if users:  # If no users, we don't need to print
        # Again handling all combinations of min_age and max_age
        # Printing the header text first
        if min_age and max_age:
            print(f'Users between {min_age} and {max_age} are:')
        elif min_age:
            print(f'Users above {min_age} are:')
        elif max_age:
            print(f'Users below {max_age} are:')
        # Printing the users
        for user in users:
            print(f"{user['first_name']} {user['last_name']}")
