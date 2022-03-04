class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        self.access_counr = 0

    @property
    def full_date(self):
        self.access_counr += 1
        return f"{self.day}-{self.month}-{self.year}"


my_date = Date(4, 3, 2022)
print(my_date.full_date)  # We access full_date without the parenthesis
my_date.full_date = '10-08-2020'
# 4-3-2022

'10-08-2020'.split('-')
