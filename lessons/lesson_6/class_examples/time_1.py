import time
import math

# Factoreal calculation
number = int(input('Number to calc factoreal'))
started_at = time.time()
acc = 1
for a in range(1, number + 1):
    acc *= a
stop_at = time.time()
print(f'My solution ran for {stop_at - started_at}, result is: {acc}')

started_at = time.time()
result = math.factorial(number)
stop_at = time.time()
print(f'Python solution ran for {stop_at - started_at}, result is: {result}')
