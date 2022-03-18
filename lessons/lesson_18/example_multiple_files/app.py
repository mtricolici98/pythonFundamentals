from flask import Flask

app = Flask(__name__)

from random_views import random_views

app.register_blueprint(random_views)  # This registers the views inside the random_views package to the application