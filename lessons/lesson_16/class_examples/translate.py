import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    'x-rapidapi-key': "REMOVED"
}

text_to_translate = input()

data = dict(
    q=text_to_translate,
    target='ru'
)

response = requests.post(url, data=data, headers=headers)

print(response.text)
