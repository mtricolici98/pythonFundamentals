from homework_solutions_lesson_8.ex_1 import test_ex_1
from homework_solutions_lesson_8.ex_2 import test_ex_2
from homework_solutions_lesson_8.ex_3 import test_ex_3
from homework_solutions_lesson_8.ex_4 import test_ex_4
from homework_solutions_lesson_8.ex_5 import test_ex_5
from homework_solutions_lesson_8.ex_extra_1 import test_ex_extra_1
from homework_solutions_lesson_8.ex_extra_2 import test_ex_extra_2
from homework_solutions_lesson_8.ex_extra_3 import test_ex_extra_3

if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: test_ex_1,
        2: test_ex_2,
        3: test_ex_3,
        4: test_ex_4,
        5: test_ex_5,
        6: test_ex_extra_1,
        7: test_ex_extra_2,
        8: test_ex_extra_3,
    }
    while True:
        # Printing after every exercise execution again
        print('Type the number of the exercise to test:')
        print('1: Ex 1')
        print('2: Ex 2')
        print('3: Ex 3')
        print('4: Ex 4')
        print('5: Ex 5')
        print('6: Extra 1')
        print('7: Extra 2')
        print('8: Extra 3')
        print('Type exit to exit the program')
        inpt = input('Exercise number: ')
        if inpt.lower() == 'exit':
            exit()
        ex_nr = int(inpt)
        exercises_map[ex_nr]()  # Executing the function at the selected number
        print('')  # Empty space for separation
