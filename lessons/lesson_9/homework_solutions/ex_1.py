def fibonacci(n):
    initial = [0, 1]
    for a in range(n):
        initial.append(initial[-1] + initial[-2])
    return initial[:-2]


# print(fibonacci(10))
