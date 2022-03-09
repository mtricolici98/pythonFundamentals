from lessons.lesson_12.homework_solutions.conversion.ConversionService import ConversionService


class CurrencyConverter:

    @staticmethod
    def initialize_conv_service(filename, base_curr='MDL'):
        conversion_service = ConversionService(base_curr)
        conversion_service.parse_file(filename=filename)
        return conversion_service

    @staticmethod
    def list_top_10(conv_service: ConversionService):
        for el in conv_service.get_list(10):
            print(el)

    @staticmethod
    def convert(conv_service: ConversionService):
        from_currency = conv_service.from_currency
        to_currency = input(
            f'To currency (from {from_currency}) '
            f'or type {from_currency} to convert to {from_currency}:'
        )
        if to_currency == conv_service.from_currency:
            to_currency = from_currency
            from_currency = input(
                'What currency you want to convert to MDL: '
            )
        amount = float(input("Amount to convert: "))
        conversion_result = conv_service.convert(from_currency, to_currency, amount)
        print(f"Converted from {from_currency} to {to_currency}: {conversion_result:.02f}")

    @staticmethod
    def handle_user_io(conv_service):
        print("Select what you want to do")
        print(f"1: List Top 10 rates")
        print(f"2: Convert")
        user_selected = input('Select: ')
        if user_selected == '1':
            CurrencyConverter.list_top_10(conv_service)
            return True
        elif user_selected == '2':
            CurrencyConverter.convert(conv_service)
            return True
        else:
            return False
