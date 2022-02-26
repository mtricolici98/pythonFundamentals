def return_list_of_lines_in_file(filename):
    file = open(filename, 'r')
    lines_list = file.readlines()
    file.close()
    return lines_list


def test_ex_extra_3():
    filename = input("Filename ?: ")
    lines = return_list_of_lines_in_file(filename)
    max_length = 0
    for line in lines:
        line_length = len(line)
        if line_length > max_length:
            max_length = line_length
    for line in lines:
        if len(line) == max_length:
            print(line)


if __name__ == '__main__':
    test_ex_extra_3()
