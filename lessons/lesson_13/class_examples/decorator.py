def printer_decorator(print_text):
    def level_1(funct):
        # Processing args for our function
        def leve_2(*args, **kwargs):
            # Passing arguments back to our function.
            value_returned = funct(*args, **kwargs)
            print(f"{print_text} {value_returned}")
            return value_returned

        return leve_2

    return level_1


@printer_decorator('Print')
def list_sum(list_of_elements):
    return sum(list_of_elements)


def list_sum_(list_of_elements):
    return sum(list_of_elements)


def print_and_reutrn(value):
    print(value)
    return value


value = print_and_reutrn(list_sum_([2, 5, 8]))

# We don't print anything here ourselves, our printer decorator will do it for us.
result = list_sum([2, 5, 8])
# 15
print(result)

USER = {}


# 15


def login_required(func):
    def check_user_is_logged_in():
        if USER:
            return True
        else:
            return False

    def wrapped_function(*args, **kwargs):
        if check_user_is_logged_in():
            func(*args, **kwargs)
        else:
            raise Exception('Not allowed, function is only for logged in users')

    return wrapped_function


@login_required
@printer_decorator
def function_only_for_users():
    pass


def file_save(filepath):
    def inner(func):
        def wrapped_function(*args, **kwargs):
            with open(filepath, 'w') as file:
                result = func(file, *args, **kwargs)
                file.write(result)
            return file

        return wrapped_function

    return inner


@file_save('example.txt')
@printer_decorator('Print')
def random_thing(file):
    file.write('something')
    return 'asd'


file = random_thing()
