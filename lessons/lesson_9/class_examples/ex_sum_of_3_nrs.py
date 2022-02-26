# 5
# 1 1 3
# 1 2 2
# 1 3 1

# A + B + C = numar
# C = numar - A - b

number = int(input("Put the number: "))
for a in range(1, number):  # O(n log n)
    for b in range(1, number - a):
        c = number - a - b
        if c > 0:
            print(a, b, c)
