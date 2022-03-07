import random


def ahead_of_time(from_, to_, numbers):
    list = []
    for a in range(numbers):
        list.append(random.randint(from_, to_))
    return list


def generator_example(from_, to_, numbers):
    for a in range(numbers):
        yield random.randint(from_, to_)



print(list(generator_example(0, 10, 10000)))

