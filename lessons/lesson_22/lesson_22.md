# Viber bots

You can find the examples [here for the scrapper with the memes](scrapper_viber_bot_example.zip)
and [here for the weather and restaurant menu](viber_bot_example.zip).

## How to run the examples

### Setup

Download and install Heroku. [Instructions here](https://devcenter.heroku.com/articles/getting-started-with-python)

Create viber bot account [here](https://partners.viber.com/account/create-bot-account)

Resources:

[Viber API](https://developers.viber.com/docs/api/rest-bot-api/#get-started)

[Viber API Python](https://developers.viber.com/docs/api/python-bot-api/#viber-api)

# Steps

After creating your bot account, please copy the Token from the bot into the config file inside the python project.

Inside the terminal (in your PyCharm) do the following. __Note: If heroku is not detected by the terminal after you
installed it, restart pycharm__

````
heroku login
````

Follow the steps to log in

```
git init
git add .
```

Your project should be now initialized as a heroku project.

```
heroku create
```

Now heroku will create a project form your account.

## Adding PostgreSQL support to heroku

Run the following command:

````
heroku addons:create heroku-postgresql:hobby-dev
````

Now your heroku server has postgresql support. Check the example [here](scrapper_viber_bot_example.zip) to see how the
database was configured.

If you want to test locally, install [PostgreSQL](https://www.postgresql.org/download/) on your computer.

Configuration inside the app should be like follows:

````python
import os

from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import declarative_base, sessionmaker

uri = os.getenv("DATABASE_URL",  # Heroku env var
                'postgresql://postgres:your_postgres_password@localhost:5432/postgres')  # postgres is the default database, you can create more databases
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
engine = create_engine(uri)

schema_name = 'viberbot'

meta = MetaData(engine, schema=schema_name)

with engine.connect() as connection:
    query = text("CREATE SCHEMA IF NOT EXISTS viberbot")
    connection.execute(query)

Base = declarative_base(engine, meta)
Session = sessionmaker(bind=engine)
````

Above, replace `your_postgres_password` with the password you set up for postgres.

If you want, you can create additional database. Example [here](https://www.guru99.com/postgresql-create-database.html)

## Running

Commit and Push your changes (your project) to git. Pushing is going to take a while, because your project will be
building.

Open your [heroku dashboard](https://dashboard.heroku.com/apps/) to see your current projects.

You can see logs, run app, and configure everything from there.
