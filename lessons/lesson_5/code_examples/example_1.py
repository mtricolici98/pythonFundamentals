numbers_dict = dict()
times = int(input('How many numbers you want to check'))
for time in range(times):
    user_number = float(input('Input a number'))
    nr_in_dict = numbers_dict.get(user_number, 0)
    numbers_dict[user_number] = nr_in_dict + 1
for number, nr_of_times_input in numbers_dict.items():
    print(f'Number {number} was used {nr_of_times_input} times')
