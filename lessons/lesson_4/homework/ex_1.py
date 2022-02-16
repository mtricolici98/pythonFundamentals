numbers = [32, 19, 39, 30]
sum = 0
even = []
for a in numbers:
    sum += a
    if a % 2 == 0:
        even.append(a)
print(f"Length of list is {len(numbers)}")
print(f"Sum is {sum}")
print(f"Even numbers are {even}")
