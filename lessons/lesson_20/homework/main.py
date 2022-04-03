import datetime

from sqlalchemy import Table, Column, String, MetaData, create_engine, BigInteger, Date, ForeignKey

# Echo parameter will print all executed statements in our console.
from lessons.lesson_20.homework.data import employee_info, project_info
from lessons.lesson_7.examples.structure_example import Project

engine = create_engine('sqlite:///python.db')

# MetaData object will hold database related information
meta = MetaData(engine)

Employees = Table(
    'employees', meta,
    Column('idnp', String(13), primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('position', String),
    Column('salary', BigInteger),
)

Projects = Table(
    'projects', meta,
    Column('name', String(13), primary_key=True),
    Column('country', String),
    Column('budget', String),
    Column('lead', String(13), ForeignKey('employees.idnp')),
    Column('year', Date),
)

meta.create_all()


# Adding initial data
def add_initial_data():
    with engine.connect() as connection:
        for employee in employee_info:
            idnp, f_n, l_n, salary, position = employee
            insert = Employees.insert().values(idnp=idnp, first_name=f_n, last_name=l_n, salary=salary,
                                               position=position)
            try:
                connection.execute(insert)
            except Exception as ex:
                pass  # Already exists
        for project in project_info:
            name, country, lead, bduget, year = project
            insert = Projects.insert().values(name=name, country=country, lead=lead, budget=bduget,
                                              year=datetime.date(year, 1, 1))
            try:
                connection.execute(insert)
            except Exception as ex:
                pass  # Already exists


def update_salary():
    with engine.connect() as connection:
        salary_update_to_position_map = {
            'Worker': 500,
            'Project manager': 1000,
            'Sale representative': 700,
            'Data Analyst': 700,
            'Administrator': 600,
            'Director': 1000,
        }
        for position, increase in salary_update_to_position_map.items():
            query = Employees.update().where(Employees.c.position == position).values(
                salary=Employees.c.salary + increase)

            connection.execute(query)


def employees_above_10000():
    with engine.connect() as connection:
        q = Employees.select().where(Employees.c.salary > 13000)
        for a in connection.execute(q).fetchall():
            print(a)


def project_managers_above_13000():
    with engine.connect() as connection:
        q = Employees.select().where((Employees.c.salary > 13000) & (Employees.c.position == 'Project manager'))
        for a in connection.execute(q).fetchall():
            print(a)


def sum_project_budget():
    with engine.connect() as connection:
        from sqlalchemy.sql.functions import sum
        q = Projects.select().group_by(Projects.c.country).with_only_columns(Projects.c.country, sum(Projects.c.budget))
        for a in connection.execute(q).fetchall():
            print(a)


def max_project_budget():
    with engine.connect() as connection:
        from sqlalchemy.sql.functions import max
        q = Projects.select().with_only_columns(Projects.c.name, max(Projects.c.budget))
        for a in connection.execute(q).fetchall():
            print(a)


def max_project_budget_year():
    with engine.connect() as connection:
        from sqlalchemy.sql.functions import max
        q = Projects.select().with_only_columns(Projects.c.year, max(Projects.c.budget))
        for a in connection.execute(q).fetchall():
            print(a)


def project_and_manager_list():
    with engine.connect() as connection:
        q = Projects.join(Employees).select().with_only_columns(Projects.c.name, Projects.c.country, Projects.c.year,
                                                                Employees.c.first_name, Employees.c.last_name)
        for a in connection.execute(q).fetchall():
            print(a)


if __name__ == '__main__':
    # update_salary()
    employees_above_10000()
    project_managers_above_13000()
    sum_project_budget()
    max_project_budget()
    max_project_budget_year()
    project_and_manager_list()
