import json
from datetime import datetime

user = {
    'username': 'Maruis',
    'password': 'badpassowrd',
    1: datetime.now().strftime('%d-%m-%Y'),
}
json_string = json.dumps(user)
print(json_string)
print(type(json_string))

my_list_file = open('my_user.json', 'w')
my_list_file.write(json_string)
my_list_file.close()

my_list_file = open('my_user.json', 'r')
data = my_list_file.read()
my_list_file.close()

user = json.loads(data)
print(user)
print(type(user))
