values_dict = dict()

dupes = 0

for i in range(10):
    value = input('Input a value:')
    if value in values_dict:
        print('I already had that one')
        dupes += 1
        values_dict[value] += 1
    else:
        values_dict[value] = 1

key_with_highest_nr = None
max_times = 0
for value, nr_of_input in values_dict.items():
    if nr_of_input > max_times:
        max_times = nr_of_input
        key_with_highest_nr = value

print(f'Total duplicates {dupes}')
print(f'Highest duplicates has value {key_with_highest_nr}, it has {max_times}')
