text = input('Input any text, please don\'t use punctuations: ')
word_list = text.split(' ')  # Splitting the text by space into separate words
word_usage_dict = {}
for word in word_list:
    if word in word_usage_dict:
        word_usage_dict[word] += 1
    else:
        word_usage_dict[word] = 1

for word, nr_of_times_used in word_usage_dict.items():
    print(f"Word {word} was used {nr_of_times_used} {'time' if nr_of_times_used == 1 else 'times'}")

