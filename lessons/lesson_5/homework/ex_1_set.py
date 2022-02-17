text = input('Input any text, please don\'t use punctuations: ')
word_list = text.split(' ')  # Splitting the text by space into separate words
unique_words = set(word_list)
for word in unique_words:
    print(f"Word {word} was used {word_list.count(word)} times")
