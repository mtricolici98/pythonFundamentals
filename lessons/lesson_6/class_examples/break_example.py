# Code that finds a person in a list of dicts
persons = [
    {'name': 'Marius', },
    {'name': 'Andrei', },
    {'name': 'Mircea', }
]
person = None
name_to_find = 'Marius'
for element in persons:
    if element['name'] == name_to_find:
        person = element
        print(f"Found {name_to_find}")
        break
    else:
        print('Not found, looking further')
