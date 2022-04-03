import json

from flask import Flask, Response, request

from lessons.lesson_12.homework_solutions.conversion.ConversionService import ConversionService

app = Flask(__name__)

rates_file = '/home/marius/PycharmProjects/pythonFundamentals/lessons/lesson_18/homework/conversion/conversion_rates.json'


@app.route('/conversions/list')
def get_conversions_list():
    curr_service = ConversionService()
    curr_service.parse_file(
        rates_file
    )
    list = curr_service.get_list()
    dict_list = [a.to_dict() for a in list]
    return Response(response=json.dumps(dict_list), status=200)


@app.route('/conversions/get/<code>', methods=['GET'])
def get_conversions_by_code(code):
    curr_service = ConversionService()
    curr_service.parse_file(
        rates_file
    )
    convertion = curr_service.find(code)
    return Response(response=json.dumps(convertion.to_dict()), status=200)


@app.route('/convert', methods=['POST'])
def convert():
    curr_service = ConversionService()
    curr_service.parse_file(
        rates_file
    )
    from_ = request.json.get('from')
    to = request.json.get('to')
    amount = request.json.get('amount')
    if not all([from_, to, amount]):
        return Response('Insufficient data', status=400)
    try:
        data = curr_service.convert(
            from_,
            to,
            amount
        )
        return Response(json.dumps(data), status=200)
    except Exception as ex:
        return Response('Bad Data', status=400)


if __name__ == '__main__':
    app.run('localhost', 5000)
