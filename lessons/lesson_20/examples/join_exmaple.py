from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')
posts_table = meta.tables.get('posts')

with engine.connect() as connection:
    join_stmt = users_table.join(posts_table).select()
    print(join_stmt)

from sqlalchemy.sql.functions import max, min, count, sum

with engine.connect() as connection:
    join_stmt = users_table.join(posts_table).select().with_only_columns(
        [users_table.c.username, count(posts_table.c.id)]
    )
    print(join_stmt)
    print(connection.execute(join_stmt).fetchall())
