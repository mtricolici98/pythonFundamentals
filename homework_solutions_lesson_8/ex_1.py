def get_type_from_input():
    data = input('Input something')  # data value will always be Int beacuse input returns int.
    value = None  # Setting value to None
    try:
        value = int(data)  # Try to convert to int
        print(f'Value {value} is an int')  # Conversion worked with no error
    except ValueError:
        pass
    if value is None:  # No result after first try
        try:
            value = float(data)  # Try to convert to float
            print(f'Value {value} is a float')  # Conversion worked with no error
        except ValueError:
            pass
    if value is None:  # Value is not assigned, this means it's not an int and not a float, this means its a string
        print(f'Value {data} is a string')


def test_ex_1():
    get_type_from_input()
