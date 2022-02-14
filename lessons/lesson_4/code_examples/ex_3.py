# Finding words that are both in the first sentence and the second sentence using sets


sentence_1 = input()
sentence_2 = input()

words_1 = set(sentence_1.split(' '))
words_2 = set(sentence_2.split(' '))

print(f"Unique words are {words_1.intersection(words_2)}")
