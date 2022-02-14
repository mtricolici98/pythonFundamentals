# Exercise String formatting

op = input('Introdu operatiunea *, /, -, +: ')
num_a = int(input('Introdu a:'))
num_b = int(input('Introdu b:'))

if op == '*':
    result = num_a * num_b
elif op == '-':
    result = num_a - num_b
elif op == '+':
    result = num_a + num_b
else:
    result = num_a / num_b

print(f"{num_a} {op} {num_b} = {result}")
