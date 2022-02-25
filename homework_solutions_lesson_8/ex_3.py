def open_file_and_print_contents(filename):
    file = open(filename, 'r') # Opening in read mode (r)
    print(file.read())
    file.close()


def test_ex_3():
    open_file_and_print_contents('ex_2_file.txt')
