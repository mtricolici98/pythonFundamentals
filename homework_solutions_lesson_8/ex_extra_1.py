import string


def count_words(text):
    # CLeaning the text
    text = text.strip()
    for el in ['\n', '\t']:  # Removing newlines, tabs, etc.. (empty space also called whitespace)
        text = text.replace(el, '')
    words = text.split(' ')
    return len(words)


def read_text_from_file(filename):
    try:
        return open(filename, 'r').read()
    except FileNotFoundError as ex:
        return None


def test_ex_extra_1():
    filename = input("Filename ?: ")
    text = read_text_from_file(filename)
    if text:
        print(f'Words count for file is {count_words(text)}')
    else:
        print(f'No text')
