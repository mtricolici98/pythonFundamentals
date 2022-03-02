import json
from json import JSONDecodeError

class FileHelper:

    def __init__(self, file_name):
        self.file_name = file_name
        self._validate_file_name()

    def _validate_file_name(self):
        if not self.file_name:
            raise Exception('No filename provided')
        if type(self.file_name) != str:
            raise Exception('Expected string as filename')

    def get_data_from_file(self):
        file = self._get_file()
        data_from_file = file.read()
        file.close()
        return data_from_file

    def save_data_to_file(self, file_data):
        file = self._get_file()
        file.write(file_data)
        file.close()

    def _get_file(self):
        try:
            file = open(self.file_name, 'r+')
        except FileNotFoundError:
            try:
                file = open(self.file_name, 'w+')
            except Exception as ex:
                print(f"Could not create file because of exception: {ex}")
                file = None
        return file


class JsonFileHelper(FileHelper):

    def __init__(self, file_name):
        super().__init__(file_name)

    def get_data(self):
        """Returns data from Json File, if no data, returns None"""
        try:
            data_from_file = self.get_data_from_file()
            return json.loads(data_from_file)
        except JSONDecodeError as ex:
            print(f'Cannot load data because of JSON error: {ex}')
            return None

    def save_data(self, data_to_save):
        try:
            data_to_file = json.dumps(data_to_save)
            self.save_data_to_file(data_to_file)
        except Exception as ex:
            print(f'Could not save data, reason {ex}')


