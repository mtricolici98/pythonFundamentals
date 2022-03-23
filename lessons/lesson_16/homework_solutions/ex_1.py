import requests


def get_api_headers():
    return {
        'x-rapidapi-key': "REMOVED"
    }


def get_all_languages():
    response = requests.get('https://google-translate1.p.rapidapi.com/language/translate/v2/languages',
                            headers=get_api_headers())
    data = response.json().get('data', {}).get('languages', [])
    return [el['language'] for el in data]


def translate(text, to_lang):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    data = dict(
        q=text,
        target=to_lang
    )
    response = requests.post(url, data=data, headers=get_api_headers())
    data = response.json().get('data')
    for element in data['translations']:
        yield element['translatedText']


def user_translate():
    all_languages = get_all_languages()
    print(f'Language options: {all_languages}')
    lang = None
    while lang not in all_languages:
        lang = input('Select a language to translate to:')
    text = input('Text to translate: ')
    for result in translate(text, lang):
        print(result)


def file_translate():
    file_path = input('File path:')
    all_languages = get_all_languages()
    print(f'Language options: {all_languages}')
    lang = None
    while lang not in all_languages:
        lang = input('Select a language to translate to:')
    with open(file_path) as f:
        text = f.read()
        for result in translate(text, lang):
            print(result)


if __name__ == '__main__':
    ex_map = {
        1: get_all_languages,
        2: user_translate,
        3: file_translate,
    }
    while True:
        print('\nSelect what you want to see:')
        print('1: List all available languages')
        print('2: Translate')
        print('3: Translate file')
        print('0: Exit()')
        choice = int(input('Choice?: '))
        if choice == 0:
            break
        ex_map[choice]()
