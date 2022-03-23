from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///python.db')
with engine.connect() as connection:
    query = text("""SELECT username, email FROM users where username = :desired_username""")
    result = connection.execute(query, desired_username='example2 or 1 = 1;')
    for line in result:
        print(line)
