def convert_to_float(string):
    try:
        return float(string)
    except ValueError:
        return None  # User input was not a float string


def main():
    maybe_number = None
    while maybe_number is None:
        maybe_number = convert_to_float(input('Input a numeric value'))
        if maybe_number is not None:
            print(f'Thanks for {maybe_number}')
        else:
            print(f'Try to input a number this time')


main()
