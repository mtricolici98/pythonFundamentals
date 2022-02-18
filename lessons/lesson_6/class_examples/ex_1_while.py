


n = int(input('Nr: '))
n_copy = n
acc = 1
if n < 1:
    print('Cant calc for this number')
else:
    while n > 1:
        acc *= n
        n -= 1
    print(acc)

if n < 1:
    print('Cant calc for this number')
else:
    acc = 1
    i = 1
    while i < (n_copy + 1):
        acc *= i
        i += 1
    print(f"{n_copy}! = {acc}")
