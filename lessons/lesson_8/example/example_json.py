import json

my_dict = {
    'name': "Marius",
    'username': "pythonguru1337",
    'password': "never_user_plaintext_password",
    'user_group': {'name': 'Admin', 'permissions': '__all__'},
}
json_string = json.dumps(my_dict)  # Creates a json string from my_dict
print(my_dict)
print(json_string)
