guest_nr = int(input('How many guests do you want to register?: '))
guest_list = []
guest_names = []
food_list = []
for _ in range(guest_nr):
    name = input('Name:')
    food_1 = input('Food 1:')
    food_2 = input('Food 2:')
    guest_list.append(
        dict(
            name=name,
            food_1=food_1,
            food_2=food_2
        )
    )
    food_list.extend([food_1, food_2])  # Adding both food 1 and food2 at the same time
    guest_names.append(name)  # Adding both food 1 and food2 at the same time

print(f'The guests will be: {guest_names}')

for guest in guest_list:
    print(f"{guest['name']} ordered {guest['food_1']} and {guest['food_2']}")

print(f'You will have to prepare')
food_set = set(food_list)
for food in food_set:
    print(f'{food} x {food_list.count(food)}')
