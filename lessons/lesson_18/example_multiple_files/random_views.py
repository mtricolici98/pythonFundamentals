import random

from flask import Blueprint, jsonify

from app import app

random_views = Blueprint('views', __name__)


@app.routes('/random/number')
def random_randint():
    return jsonify(random.randint(1, 100))


@app.routes('/random/list')
def random_randint():
    lst = []
    for a in range(10):
        lst.append(random.randint(1, 100))
    return jsonify(lst)