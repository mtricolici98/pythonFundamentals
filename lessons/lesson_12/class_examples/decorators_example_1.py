class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        return cls(*map(int, date_as_string.split('-')))

    @staticmethod
    def static_from_string(date_as_string):
        return Date(*map(int, date_as_string.split('-')))

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


class OtherDate(Date):
    pass


print(Date.is_date_valid("02-03-2022"))
print(Date.from_string("02-03-2022"))
print(OtherDate.from_string("02-03-2022"))
print(OtherDate.static_from_string("02-03-2022"))
