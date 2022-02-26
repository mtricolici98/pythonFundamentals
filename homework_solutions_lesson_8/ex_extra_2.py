import string

from homework_solutions_lesson_8.ex_extra_1 import read_text_from_file


def count_each_word(text):
    chars = dict()
    for char in text:
        if char not in string.punctuation and char not in string.whitespace:
            chars[char] = chars.get(char, 0) + 1
    return chars


def test_ex_extra_2():
    filename = input("Filename ?: ")
    text = read_text_from_file(filename)  # Reusing from previous exercise
    if text:
        char_dict = count_each_word(text)
        for char, count in char_dict.items():
            print(f"Char {char}: {count} times")
    else:
        print(f'No text')


if __name__ == '__main__':
    test_ex_extra_2()
