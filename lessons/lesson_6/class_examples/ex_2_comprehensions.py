

urs_str = input('Type a sentence: ')
words_list = urs_str.split(' ')

lowercase_word_list = [word.lower() for word in words_list]
longer_than_5_char = [word for word in words_list if len(word) >= 5]

print(lowercase_word_list)
print(longer_than_5_char)