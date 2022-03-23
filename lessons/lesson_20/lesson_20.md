# Working with Databases in Python

Python, like many other languages makes it very easy to work with SQL.

To do so, we need to install the appropriate library.

The most popular SQL Library in python is SQLAlchemy.

## SQLAlchemy

SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. It is written in Python and gives full power and
flexibility of SQL to an application developer.

It allows us to easily perform SQL operations in python.

## ORM

Object-Relational Mapping (ORM) is a technique that lets you query and manipulate data from a database using an
object-oriented paradigm.

Basically ORM allows us to represent values in our SQL tables as objects in python, and work with them as such.

We will learn more advanced ORM techniques in our next lessons.

## Installing SQLAlchemy

Installing is done using PIP: `pip install sqlalchemy`

## Connecting to a database

In order to create to a database we should create a database engine inside our python application.

This is done using the **create_engine()** function

````python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///my_first_database.db')
````

The example above creates a connection to an SQLite database. As we discussed last lesson, SQLite database are stored in
files.

The create_engine argument has the following structure: `dialect+driver://user:pass@host:port/db`.

Applying the structure to our example, we get the following breakdown:

* The `sqlite://` part defines the type of database connection, for us it's sqlite
* The `/my_first_database.db` part defines the path to the database file

Using another example: a different type of database, example MySql, it would be the following.

`mysql+pymysql://user:pass@some_my_sql_address/databasename?charset=utf8mb4`

* The `mysql` part defines the type of database, whereas the `+pymysql` part defines the driver to use. The driver is a
  software library that will manage the communication with the database. Some databases can have multiple drivers. If no
  driver is specified, SQLAlchemy will use a default driver for the selected database.
* The `user:pass` part defines our authentication parameters, mysql and other databases require authentication in order
  to connect to the database.
* `@some_my_sql_address` refers to the location of the SQL server, this could be either an IP address `192.0.0.1` or a
  domain name `company_database.company.com`
* `/databasename` refers to the actual database inside the server. SQL servers might have multiple databases

## Querying the database.

The most basic way to query a SQL database with SQLAlchemy is through the connection itself.

This allows us to query items using raw sql.

Consider the example below

````python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///my_first_database.db')
with engine.connect() as connection:
    query = text("""SELECT username, email FROM users""")
    result = connection.execute(query)
    print(result)
    # <sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000018383765030>
    for line in result:
        print(line)
    # ('user1', 'user1@email.com')
    # ('user2', 'user2@email.com')
    # ('user3', 'user3@email.com')
    # ('user4', 'user4@email.com')
    # ('user5', 'user5@email.com')
    # ('user6', 'user6@email.com')
    # ('user7', 'user7@email.com')
````

In the example above, we declare our query. You see that our query is not just a string, but it's a **text** object.

This **text** object is used to hold our SQL Query. At a basic level, it provides us with the ability to parametrize our
SQL query.

The result of a query execution will be an iterable result. That can be iterated as a result of tuples. Where each value
in the tuple corresponds to a column in the table.

Let's now do the same, but with a parametrised WHERE statement.

```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///my_first_database.db')
with engine.connect() as connection:
    # Introducing a placeholder value in our statement
    query = text("""SELECT username, email FROM users where username = :desired_username""")
    # Filling that placeholder value with an actual value
    result = connection.execute(query, desired_username='user1')
    for line in result:
        print(line)
    # ('user1', 'user1@email.com')
```

Same as with the previous example, this statement returned an iterable that holds our result.

We can execute any type of query using the **connection.execute()** method. Insert, update, delete, and even create or
drop table.

The execute command acts like a query console, where we can send commands to our database.

Last example, a INSERT statement using the execute command.

```python
from datetime import datetime

from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///my_first_database.db')
with engine.connect() as connection:
    query = text("""
    INSERT into users (username, email, registration_date)
     values (:un, :email, :reg_date)
     """)
    result = connection.execute(query,
                                un='Username',
                                email='example@email.com',
                                reg_date=datetime.now().date())
    print(result.rowcount)  # Number of affected records - 1
```

This example, will insert a new record in our database.

If an error happens in the database, we will receive an exception. For example, when the username already exists.

Also, you may have noticed that for the `registration_date` argument we passed `datetime.now()`. In this case, the
database or SQLAlchemy will do the conversion to the proper value format automatically.

## The easier way of working with Databases

Now that we know the long way around, that is, working using raw queries, let's take a look at the more Pythonistic way
we can work with such databases using Python and SQLAlchemy.

SQLAlchemy provides us with the ability to declare tables and create structures directly using python objects.

For the following examples, we will use a new (clean) database.

Consider the following example:

```python
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

# Echo parameter will print all executed statements in our console.
engine = create_engine('sqlite:///python.db', echo=True)

# MetaData object will hold database related information
meta = MetaData(engine)

users = Table(
    'users', meta,  # Meta passed as argument here
    Column('id', Integer, primary_key=True),
    Column('username', String),
    Column('email', String),
)

meta.create_all()
```

Let's break down what happens above:

1. We create an engine, with a new database in it.
2. We declare an object, meta, which is a MetaData object. The metadata object basically contains all the information
   about our tables in our database.
    1. We also bind our database engine to the meta (by passing it as an argument), so that meta can access the data
       from the database.
3. We declare a new table.
    1. The first argument is the name fo the table.
    2. The second argument is the meta object. This is passed so that the table can be registered inside the metadata
       object.
    3. The columns we want to add to our database. We can see that definition of the columns is pretty straight forward,
       we can declare data types, column names, and even constraints using the Column object.
4. We ask the meta object to create all the tables.

If we look at the output of our program, we would see the query that SQLAlchemy used to create our table.

```
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	email VARCHAR, 
	PRIMARY KEY (id)
)
```

In case the table already exists. The **create_all()** function will do nothing. Not even if the table definition is
changed, for example, you've added or removed a column.

### Column data types

SQLAlchemy tries to match the datatypes available in SQL, thus many data types we discussed previously are also
available using SQLAlchemy.

Those types include **BigInteger**, **Boolean**, **Date**, **DateTime**, **Float**, **Integer**, **Numeric**,
**SmallInteger**, **String**, **Text**, **Time**, and others. See full
list [here](https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types)

When defining a column we should declare a column name (the first argument) and a column type (the second argument).

```python
Column('column_name', ColumnType)
```

Other arguments can be provided:

| Argment         | Explanation                           | Values                         |
|-----------------|---------------------------------------|--------------------------------|
| `primary_key`   | Is the column a primary key           | True / False                   |
| `nullable`      | Null values allowed                   | True / False                   |
| `unique`        | Allows only unique values             | True / False                   |
| `default`       | Specifies default value for the field | value that matches column type |
| `autoincrement` | Should the field autoincrement        | True / False                   |

## Accessing an existing table

We can access tables that already exist in the database using the **reflect** function of the meta object.

The reflect function will inspect the database and populate the **meta** object with all the database information.

```python
from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')

meta = MetaData(engine)
# Loading info from our database
meta.reflect()

print(meta.tables)
# FacadeDict({'users': Table('users', MetaData(bind=Engine(sqlite:///python.db))....
```

We can easily access the table inside the tables property of our meta.

```python
users_table = meta.tables.get('users')
print(users_table.columns)
# ImmutableColumnCollection(users.id, users.username, users.email)
```

## Querying data from the table

SQLAlchemy gives us access to expression that mimic the functionalities of SQL, but using methods and functions instead
of SQL statements.

```python
from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
user_table = meta.tables.get('users')

with engine.connect() as connection:
    # Creates an expression
    select_expression = user_table.select()
    print(select_expression)
    # SELECT users.id, users.username, users.email
    # FROM users
    result = connection.execute(select_expression)
    for a in result:
        print(a)
    # (1, 'example1', 'example@email.com')
    # (2, 'example2', 'another@email.com')
```

SQL Expression created by SQLAlchemy need to be executed using the connection, similar to how we executed raw python
previously.

The results of these select expressions will also be iterables with tuples inside.

We can also get the first element by calling a method called "fetchone".

```python
with engine.connect() as connection:
    select_expression = user_table.select()
    result = connection.execute(select_expression)
    single_result = result.fetchone()
    print(single_result)
    # (1, 'example1', 'example@email.com')
```

### More complex queries

We can use expressions like this to create complex queries as well, with group by's, where conditions and more.

```python
with engine.connect() as connection:
    select_expression = user_table.select().where(user_table.c.id == 1).group_by('username')
    print(select_expression)
    # SELECT users.id, users.username, users.email
    # FROM users
    # WHERE users.id = ? GROUP BY users.username
    result = connection.execute(select_expression)
    single_result = result.fetchone()
    print(single_result)
    # (1, 'example1', 'example@email.com')
```

In the example above we can see that passing we can add where and group_by statements, as well as having and order_by
statements if needed.

This in terms creates a different query that applies the additional conditions.

One thing to note, is that inside out **where** condition we have provided a comparison between a column inside our
table and a value. We can access the columns from our table using the **table_name.c.column_name** syntax.

Besides, simple comparison operations, such as '>' , '<', '==' we can also perform 'LIKE' operations.

This is done by calling a **like** function on the column.

````python
with engine.connect() as connection:
    select_expression = user_table.select().where(user_table.c.username.like('example%'))
    print(select_expression)
    # SELECT users.id, users.username, users.email
    # FROM users
    # WHERE users.id = ? GROUP BY users.username
    result = connection.execute(select_expression)
    single_result = result.fetchall()
    print(single_result)
    # [(1, 'example1', 'example@email.com'), (2, 'example2', 'another@email.com')]
````

We can also have multiple statements inside our where condition. We can combine those using **&** (for or) and **&** (
for and) symbols.

```python
select_expression = user_table.select().where(
    (user_table.c.username == 'example1') | (user_table.c.email.like('%@email.com'))
)
# SELECT users.id, users.username, users.email
# FROM users
# WHERE users.username = ? OR users.email LIKE ?
select_expression = user_table.select().where(
    (user_table.c.username == 'example1') & (user_table.c.email.like('%@email.com'))
)
# SELECT users.id, users.username, users.email
# FROM users
# WHERE users.username = ? AND users.email LIKE ?
```

## Inserting data

Inserting data can be done using practically the same way. We can use the insert() method on our table to insert data.

```python
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
    # [(1, 'example1', 'example@email.com'),
    # (2, 'example2', 'another@email.com'),
    # (3, 'new user', 'Email@gmail.com')] # New record added
```

The insert method takes the values as a dictionary for an argument.

We can also pass a list of dicts, to insert multiple values at the same time.

```python
with engine.connect() as connection:
    insert_statement = users_table.insert([dict(id='4', username='another user', email='somemail@gmail.com'),
                                           dict(id='5', username='yet another', email='nomail@gmail.com')])
    print(insert_statement)
    # INSERT INTO users (id, username, email) VALUES (?, ?, ?), (?, ?, ?)
    connection.execute(insert_statement)
    print(connection.execute(users_table.select()).fetchall())
    # [(1, 'example1', 'example@email.com'),
    # (2, 'example2', 'another@email.com'),
    # (3, 'new user', 'Email@gmail.com'),
    # (4, 'another user', 'somemail@gmail.com'),
    # (5, 'yet another', 'nomail@gmail.com')]
```

## Updating and deleting data

Updating and deleting data, similarly to the insert statements are done rather easily.

For this we use the **update** or **delete** method, together with the **where()** method if the case

The **update** method takes the values to change as keyword arguments for the **values** function. The values function
can be considered the **SET** clause of the SQL statement.

````python
with engine.connect() as connection:
    update_statement = users_table.update().where(users_table.c.id == 3).values(username='superuser')
    print(update_statement)
    # UPDATE users SET username=? WHERE users.id = ?
    delete_statement = users_table.delete().where(users_table.c.id == 4)
    print(delete_statement)
    # DELETE FROM users WHERE users.id = ?
    connection.execute(update_statement)
    connection.execute(delete_statement)
````

To make sure the data is updated and deleted, we can query the database for it:

```python
with engine.connect() as connection:
    print(connection.execute(users_table.select().where(users_table.c.id == 3)).fetchone())
    # (3, 'superuser', 'Email@gmail.com')
    print(connection.execute(users_table.select().where(users_table.c.id == 4)).fetchone())
    # None
```

## Joins

Joins are also possible in SQLAlchemy, and are done with relative ease.

In order to have something to join, I'm going to create a new table, called Posts.

````python
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')

posts_table = Table(
    'posts', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('title', String),
    Column('message', String),
    Column('user', ForeignKey(users_table.c.id))
)

meta.create_all()
````

Now let's add some data to the posts table

```python
from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')
posts_table = meta.tables.get('posts')

with engine.connect() as connection:
    connection.execute(posts_table.insert([
        dict(title='Title 1', message='Message 1', user=1),
        dict(title='Title 2', message='Message 2', user=1),
        dict(title='Title 3', message='Message 3', user=1),
        dict(title='Title 4', message='Message 4', user=2),
    ]))
```

Now that we have some data in our table, let's work with some joins.

SQLAlchemy is aware of the foreign key relationships between tables, and thus can automatically perform joins without us
specifying the **ON** clause.

```python
from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///python.db')
meta = MetaData(engine)
meta.reflect()
users_table = meta.tables.get('users')
posts_table = meta.tables.get('posts')

with engine.connect() as connection:
    join_stmt = users_table.join(posts_table).select()
    print(join_stmt)
    # SELECT users.id, users.username, users.email,
    #        posts.id AS id_1,
    #        posts.title, posts.message, posts.user
    # FROM users JOIN posts ON users.id = posts.user
```

As you can se above, a join statement is very easy to achieve.

We can also perform aggregations on this data, with relative ease:

Aggregations should be available by importing them from `sqlalchemy.sql.functions`

```python
from sqlalchemy.sql.functions import count

with engine.connect() as connection:
    join_stmt = users_table.join(posts_table).select().with_only_columns(
        [users_table.c.username, count(posts_table.c.id)]
    )
    print(join_stmt)
    # SELECT users.username, count(posts.id) AS count_1 
    # FROM users JOIN posts ON users.id = posts.user
    print(connection.execute(join_stmt).fetchall())
    # [('example1', 4)]
```

Other aggregator functions include min, max, sum and many
more. [See here](https://docs.sqlalchemy.org/en/14/core/functions.html)

## Modifying tables

As you can see we have not discussed modifying tables using SQLAlchemy. That's because SQLAlchemy does not support table
modificaiton by default.

This can still be done using a separate
library [sqlalchemy-migrate](https://sqlalchemy-migrate.readthedocs.io/en/v0.7.1/changeset.html)

If you are interested, check it out yourself.

## Re-creating test database

In this lesson I will be using for a moment a database I have previously created, that holds all the records and tables
that are being queried.

You can either download this database (it will be provided with the lesson), or you can create your own.
