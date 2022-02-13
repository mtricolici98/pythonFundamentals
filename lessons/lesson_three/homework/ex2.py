n1 = float(input('Number 1'))
n2 = float(input('Number 2'))
highest = n1 if n1 > n2 else n2
print(highest)

# Longer version

n1 = float(input('Number 1'))
n2 = float(input('Number 2'))
if n1 > n2:
    print(n1)
else:
    print(n2)
