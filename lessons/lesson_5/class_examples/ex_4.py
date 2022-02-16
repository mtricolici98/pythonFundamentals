# How many times was a value was input from console after N inputs

names_dict = dict()

times = int(input('How many numbers ? '))

for i in range(times):
    name = input('Gimme name')
    times_in_dict = names_dict.get(name, 0)
    names_dict[name] = times_in_dict + 1

for number, nr_of_input in names_dict.items():
    print(f'Number {number} was used {nr_of_input} times')
