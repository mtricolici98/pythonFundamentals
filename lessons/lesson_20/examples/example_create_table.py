from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

# Echo parameter will print all executed statements in our console.
engine = create_engine('sqlite:///python.db', echo=True)

# MetaData object will hold database related information
meta = MetaData(engine)

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String),
    Column('email', String),
)

meta.create_all()
