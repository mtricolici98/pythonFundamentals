from datetime import datetime, date


class Human:

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        if type(date_of_birth) is not date:
            self._convert_string_date(date_of_birth)
        else:
            self.date_of_birth = date_of_birth

    def _convert_string_date(self, date):
        self.date_of_birth = datetime.strptime(date, '%d/%m/%Y').date()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        now = datetime.now()
        years = now.year - self.date_of_birth.year
        if now.month <= self.date_of_birth.month and now.day < self.date_of_birth.day:
            years -= 1
        return years

    def __str__(self):
        return f'{self.get_full_name()}, age {self.get_age()}'
