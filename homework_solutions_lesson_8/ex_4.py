from homework_solutions_lesson_8.ex_2 import create_file
from homework_solutions_lesson_8.ex_3 import open_file_and_print_contents


def create_file_and_fill_with_input():
    file_name = input('Type the file name to create')
    create_file(file_name)  # Reusing function from previous exercise
    data = input('Type what you want to add to the file')
    file = open(file_name, 'w')  # Opening in write mode (w)
    file.write(data)
    file.close()
    open_file_and_print_contents(file_name)  # Re-using function from previous exercise


def test_ex_4():
    create_file_and_fill_with_input()
