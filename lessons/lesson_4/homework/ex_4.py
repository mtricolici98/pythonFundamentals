# Factorial example

nr = int(input('Number'))

if nr < 1:
    print(f'Cannot calculate factorial for {nr}')
else:
    accumulator = 1
    for a in range(1, nr + 1):
        accumulator *= a
    print(accumulator)
