from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')

with engine.connect() as connection:
    insert_statement = users_table.insert(dict(id='3', username='new user', email='Email@gmail.com'))
    print(insert_statement)
    # INSERT INTO users (id, username, email) VALUES (?, ?, ?)
    connection.execute(insert_statement)
    print(connection.execute(users_table.select()).fetchall())

with engine.connect() as connection:
    insert_statement = users_table.insert([dict(id='4', username='another user', email='somemail@gmail.com'),
                                           dict(id='5', username='yet another', email='nomail@gmail.com')])
    print(insert_statement)
    # INSERT INTO users (id, username, email) VALUES (?, ?, ?), (?, ?, ?)
    connection.execute(insert_statement)
    print(connection.execute(users_table.select()).fetchall())
