from lessons.lesson_12.homework_solutions.conversion.CurrencyConverter import CurrencyConverter


def main():
    conv_service = CurrencyConverter.initialize_conv_service('conversion_rates.json', 'MDL')
    while True:
        result = CurrencyConverter.handle_user_io(conv_service)
        if not result:
            break


main()
