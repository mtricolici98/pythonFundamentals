import datetime
import json


def get_data_from_file(filename):
    file = open(filename, 'r')
    return file.read()


def get_json_data_list(filename):
    data = get_data_from_file(filename)
    json_data = json.loads(data)
    return json_data


def list_properties_in_list_of_dicts(list_of_dicts, property):
    """Function that returns a list with all values from a key in a dict"""
    return [element[property] for element in list_of_dicts]


def get_employee_name_list(from_data):
    return list_properties_in_list_of_dicts(from_data, 'name')  # getting all names form the data list


def get_positions_set(from_data):
    return list(set(list_properties_in_list_of_dicts(from_data, 'position')))  # Making the values unique


def get_total_salary(from_data):
    return sum(list_properties_in_list_of_dicts(from_data, 'salary'))


def get_tax_for_salary(from_data):
    tax = float(input('Input the tax value (%): '))
    return get_total_salary(from_data) / (tax / 100)


def get_top_paid(from_data, nr_of_employees):
    sorted_salaries = sorted(list_properties_in_list_of_dicts(from_data, 'salary'), reverse=True)
    top_paid = []
    for element in from_data:
        if len(top_paid) == nr_of_employees:
            break
        if element['salary'] in sorted_salaries:
            top_paid.append(element)
    return top_paid


def get_top_oldest(from_data, number_of_employees):
    dates = list_properties_in_list_of_dicts(from_data, 'employee_from')
    datetime_dates = [datetime.datetime.strptime(date, '%m/%d/%Y') for date in dates]
    sorted_dates = sorted(datetime_dates)
    top_oldest = sorted_dates[:number_of_employees]
    converted_top_10_dates = [date.strftime('%m/%d/%Y') for date in top_oldest]
    top_oldest_employees = []
    for element in from_data:
        if len(top_oldest_employees) == number_of_employees:
            break
        if element['employee_from'] in converted_top_10_dates:
            top_oldest_employees.append(element)
    return top_oldest_employees


def print_top_10_paid(from_data):
    for el in get_top_paid(from_data, 10):
        print(f"Employee {el['name']}, salary {el['salary']}")


def print_top_10_oldest(from_data):
    for el in get_top_oldest(from_data, 10):
        print(f"Employee {el['name']}, from {el['employee_from']}")


if __name__ == '__main__':
    data = get_json_data_list('employee_list.json')
    ex_map = {
        1: get_employee_name_list,
        2: get_positions_set,
        3: get_total_salary,
        4: get_tax_for_salary,
        5: print_top_10_paid,
        6: print_top_10_oldest
    }
    while True:
        print('Select what you want to see:')
        print('1: List of all employees')
        print('2: List of all positions')
        print('3: Total salary')
        print('4: Total tax')
        print('5: Top 10 paid employees')
        print('6: Top 10 oldest employees')
        print('0: Exit()')
        choice = int(input('Choice?: '))
        if choice == 0:
            break
        result = ex_map[choice](data)  # Some of our functions return results (get functions)
        if result:
            if type(result) == list:  # Some of those results may be a list
                for element in result:  # Printing entire list
                    print(element)
            else:
                print(result)  # Single result, print it instead
