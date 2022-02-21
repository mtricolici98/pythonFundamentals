


def input_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(
            int(input('Input a number: '))
        )
    return numbers


for a in input_numbers(5):
    print(a)
