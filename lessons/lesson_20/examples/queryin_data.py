from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
user_table = meta.tables.get('users')

with engine.connect() as connection:
    select_expression = user_table.select()
    print(select_expression)
    result = connection.execute(select_expression)
    for a in result:
        print(a)
    result = connection.execute(select_expression)
    single_result = result.fetchone()
    print(single_result)

with engine.connect() as connection:
    select_expression = user_table.select().where(user_table.c.username.like('example%'))
    result = connection.execute(select_expression)
    print(result.fetchall())
    print(result.fetchone())
    print(result.fetchall())
#
with engine.connect() as connection:
    select_expression = user_table.select().where(
        (user_table.c.username == 'example1') | (user_table.c.email.like('%@email.com'))
    )
    select_expression = user_table.select().where(
        (user_table.c.username == 'example1') & (user_table.c.email.like('%@email.com'))
    )
    result = connection.execute(select_expression)
    single_result = result.fetchall()
    print(single_result)
