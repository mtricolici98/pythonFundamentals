example = {'employee': {'data': {'personal_data': {'first_name': 'Marius'}}}}


print(example.get('employees', None))

# first_name = example['employee']['data']['personal_data']['last_name']

# print(first_name)

import pydash as py_

a = py_.get(example, 'employee.data.personal_data.last_name')
print(a)

py_.set_(example, 'employee.data.personal_data.last_name', 'Tricolici')
a = py_.get(example, 'employee.data.personal_data.last_name')
print(a)

print(example)