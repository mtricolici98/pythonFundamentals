from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')

with engine.connect() as connection:
    update_statement = users_table.update().where(users_table.c.id == 3).values(username=users_table.c.username + '1')
    connection.execute(update_statement)
    print(connection.execute(users_table.select()).fetchall())
