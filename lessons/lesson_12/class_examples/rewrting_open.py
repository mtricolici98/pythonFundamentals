class open_file:

    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.file.closed)
        self.file.close()
        return False


with open_file('some_file.txt', 'w+') as file:
    file.write(input('data'))
    file.close()
