def create_file(filename):
    try:
        open(filename, 'x')  # mode x allows us to create files
    except FileExistsError:
        print("File already existed.")


def test_ex_2():
    file_name = input('Type the file name to create')
    create_file(file_name)
