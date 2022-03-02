from datetime import datetime, date


class Human:

    def __init__(self, first_name, last_name, date_of_birth: date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = datetime.now().date()
        years = today.year - self.date_of_birth.year
        if today.month <= self.date_of_birth.month and today.day < self.date_of_birth.day:
            years -= 1
        return years

    def __str__(self):
        return f"{self.get_full_name()}, age {self.get_age()}"
