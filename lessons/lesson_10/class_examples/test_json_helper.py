from JsonFileHelper import JsonFileHelper

file_name = 'example.json'

helper = JsonFileHelper(file_name)
print(helper.get_data())