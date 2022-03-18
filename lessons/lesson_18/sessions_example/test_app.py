import json

from requests import Session

my_session = Session()
r = my_session.post(
    'http://127.0.0.1:5000/login', data=json.dumps({
        'username': 'Marius'
    }),
    headers={'Content-type': 'application/json'}
)
response = my_session.get('http://127.0.0.1:5000/who-is')
print(response.content)
