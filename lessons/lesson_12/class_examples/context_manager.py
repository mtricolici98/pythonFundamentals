import random
import time


class ignore_no_file_error:

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


with ignore_no_file_error():
    sum = 0
    for a in range(10000):
        for b in range(10):
            sum += a + b
    print(sum)
    raise_exception = random.randint(0, 1)

print('Heyo, im here')


class open_file:

    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.file.closed:
            self.file.close()


with open_file('some_file.txt', 'w+') as file:
    file.write(input('data'))
