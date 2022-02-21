## BAD
def main():
    n = int(input('How many times ? '))
    inpt_list = []
    for i in range(n):
        inpt_list.append(
            input('Write your input')
        )
    lower_inpt_lsit = [i.lower() for i in inpt_list]
    for input in lower_inpt_lsit:
        print(input)


## GOOD
def user_input_times():
    return int(input('How many times? '))


def get_multiple_user_inputs(nr_of_inputs):
    inpt_list = []
    for i in range(nr_of_inputs):
        inpt_list.append(
            input('Write your input')
        )
    return inpt_list


def print_many(list_to_print):
    for el in list_to_print:
        print(el)


def main_2():
    user_input = get_multiple_user_inputs(user_input_times())
    lower_user_input = [inpt.lower() for inpt in user_input]
    print_many(lower_user_input)
