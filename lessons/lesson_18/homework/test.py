import requests


def test_list():
    data = requests.get('http://localhost:5000/conversions/list')
    print(data.json())


def test_get():
    data = requests.get('http://localhost:5000/conversions/get/EUR')
    print(data.json())


def test_convert():
    data = requests.post('http://localhost:5000/convert',
                         json={
                             'from': 'MDL',
                             'to': 'EUR',
                             'amount': 2000
                         })
    print(data.json())


if __name__ == '__main__':
    test_list()
    test_get()
    test_convert()
