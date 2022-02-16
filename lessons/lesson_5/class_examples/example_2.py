guest_list = list()

times = int(input('How many people you want to register'))

for n in range(times):
    name = input('What is the guest name ? ')
    gender = input('What is the guests gender ? (M/F) ')
    food_preference = input('What is the guests food of choice ?')
    guest = dict(
        name=name,
        gender=gender,
        food_preference=food_preference
    )
    guest_list.append(guest)

# Let's print out all guests that are female
for guest in guest_list:
    if guest['gender'] == 'F':
        print(f'{guest["name"]} is female')
