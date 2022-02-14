# Sorting 5 numbers input by user to two different lists based on them being even or odd


even = list()
odd = []
for _ in range(5):
    nr = int(input('Gimme number'))
    if not nr % 2:
        even.append(nr)
    else:
        odd.append(nr)
print(f'Even numbers are {even}')
print(f'Odd numbers are {odd}')
