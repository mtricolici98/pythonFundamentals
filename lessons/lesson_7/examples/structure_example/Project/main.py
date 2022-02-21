from lessons.lesson_7.examples.structure_example.Project.project_utils import database_utils
from lessons.lesson_7.examples.structure_example.Project.services import file_utils, database_service


def main():
    database_dat = database_utils.process_query_results(database_service.query_database('Some query'))
    file = file_utils.create_file('data.json')
    file_utils.write_to_file(file, database_dat)
    file.close()


if __name__ == '__main__':
    main()
