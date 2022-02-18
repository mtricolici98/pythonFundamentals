from datetime import datetime

print(datetime.now())

from datetime import datetime, timedelta

date_today = datetime(2022, 2, 18, 18, 30)  # Declaring a datetime object
date_yesterday = datetime(2022, 2, 17)  # Declaring a datetime object without time
print(date_today - date_yesterday)  # 1 day, 18:30:00 - Result is a timedelta

in_one_day = timedelta(days=1)  # Declaring a custom timedelta
one_day_from_now = datetime.now() + in_one_day # Operations with timedelta
if one_day_from_now > datetime.now(): # Operations with datetime
    print(f'{one_day_from_now} is in the future')

from datetime import time, date

human_time = time(12, 30)
print(human_time)  # 12:30:00
human_date = date(2022, 12, 31)
print(human_date)  # 2022-12-31
