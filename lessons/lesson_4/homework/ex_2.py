times = int(input('How many numbers ?'))
sum = 0
numbers = []
for a in range(times):
    nr = float(input('Input a number'))
    sum += nr
    numbers.append(nr)
divide_by = times if times else 1  # Avoiding division by 0
print(f'Average is {sum / divide_by}')
divide_by = len(numbers) if numbers else 1  # Avoiding division by 0
print(f'Average is {sum / divide_by}')
