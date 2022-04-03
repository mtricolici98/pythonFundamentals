import json

from lessons.lesson_12.homework_solutions.conversion.Conversion import Conversion


class ConversionService:

    def __init__(self, from_currency='MDL'):
        self._conversions = []
        self.from_currency = from_currency

    def parse_file(self, filename):
        self._conversions = []  # Initializing a new list
        try:
            with open(filename) as file:
                data = json.loads(file.read())
        except json.JSONDecoder:
            print('File data is not formatted properly, cannot processa')
        for key, element in data.items():
            self._conversions.append(Conversion.from_dict(element, self.from_currency))
        self._conversions = sorted(self._conversions)

    def convert(self, from_currency: str, to_currency: str, amount):
        revesed = True if to_currency == self.from_currency else False
        if revesed:
            conversion = self.find(from_currency)
            return amount * conversion.inverseRate
        else:
            conversion = self.find(to_currency)
            return amount * conversion.rate

    def get_list(self, top=None):
        return self._conversions[:top]

    def find(self, to_currency):
        for conversion in self._conversions:
            if conversion.from_curr == self.from_currency and conversion.to_curr == to_currency:
                return conversion
