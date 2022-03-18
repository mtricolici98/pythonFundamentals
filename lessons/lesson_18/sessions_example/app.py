from flask import Flask, request, session, make_response, jsonify

app = Flask(__name__)
app.secret_key = b'lkj12h4oiu1-9sdaujbfi1u3h813h5913'  # Random secret key


@app.route('/login', methods=['POST'])
def login():
    username = request.get_json().get('username')
    if username:
        session['user'] = username
    return make_response({}, 200)


@app.route('/who-is', methods=['GET'])
def who_is_the_user():
    return jsonify(session.get('user'))
