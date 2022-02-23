import json

my_dict = {
    'name': "Marius",
    'username': "pythonguru1337",
    'password': "never_user_plaintext_password",
    'user_group': {'name': 'Admin', 'permissions': '__all__'},
}
json_string = json.dumps(my_dict)  # Creates a json string from my_dict
file = open('user.json', 'w+')
file.write(json_string)
file.close()

file = open('user.json', 'r+')
json_string = file.read()
data = json.loads(json_string)
print(data)
