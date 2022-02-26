import json
import random
import time


# Code I copied from the internet
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


names = [
    'Eoin Senior',
    'Keyan Edwards',
    'Everett Heaton',
    'Tate Richards',
    'Kacy Mccray',
    'Marina Pugh',
    'Evie-Grace Couch',
    'Raveena Graham',
    'Kirby Bennett',
    'Sharna Vega',
    'Shiv Hayward',
    'Elmer Rodgers',
    'Debra Evans',
    'Gordon Jacobson',
    'Joely Nielsen',
    'Mikhail Beil',
    'Kaitlyn Butt',
    'Edwin Cordova',
    'Earl Greig',
    'Mahek Wharton',
    'Hebe Sierra',
    'Cali Sanchez',
    'Myron Downs',
    'Mackenzie Morrison',
    'Garfield Kelly',
    'Hamid Jacobs',
    'Isma Rawlings',
    'Jarvis Hodson',
    'Malak Burns',
    'Brandy York',
    'Tyra Haney',
    'Sila Mcknight',
    'Imogen Metcalfe',
    'Timur Peck',
    'Martin Mcdougall',
    'Diya Sweet',
    'Adrian Powell',
    'Sophie Snyder',
    'Giovanni Cowan',
    'Lani Grey',
    'Subhaan Robson',
    'Emir Britton',
    'Milena Mansell',
    'Nico Frank',
    'Yousuf Bauer',
    'Freya Arias',
    'Roseanna Rodriguez',
    'Shayan Rhodes',
    'Viktoria Stokes',
    'Elias Mcculloch',
]

positions = [
    'Administrative Assistant',
    'Executive Assistant',
    'Marketing Manager',
    'Customer Service Representative',
    'Nurse Practitioner',
    'Software Engineer',
    'Sales Manager',
    'Data Entry Clerk',
]


def generate_employee(name_idx):
    return dict(name=names[name_idx], position=positions[random.randint(0, 7)],
                salary=random.randint(1000, 4000), employee_from=random_date("1/1/2008", "1/1/2020", random.random()))


employees = []

for a in range(50):
    employees.append(generate_employee(a))

with open('../employee_list.json', 'w') as file:
    employees_rep = [employee for employee in employees]
    file.write(json.dumps(employees_rep))
