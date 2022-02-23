def ex_1():
    user_string = input('Type text to check if it\'s palindrome')
    user_string = user_string.replace(' ', '')  # Remvoing spaces
    char_list = list(user_string)
    char_list.reverse()  # Reversing char list
    reversed_string = "".join(char_list)  # Joining elements of list to a new string
    if user_string == reversed_string:
        print('Text is palindrome')
    else:
        print('Text is not palindrome')


def ex_2():
    from utils.number_utils import is_number_prime
    number = int(input('Enter a number to check if it\'s prime'))
    if is_number_prime(number):
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')


def ex_3_1():
    from utils.number_utils import number_is_perfect
    input_int = int(input('Please enter numbet to check if it\'s perfect'))
    if number_is_perfect(input_int):
        print(f'{input_int} is perfect')
    else:
        print(f'{input_int} is not perfect')


def ex_3_2():
    from utils.number_utils import number_is_perfect
    input_int = int(
        input('How many perfect numbers would you like ? If you want more than 4 prepare to wait a long time: ')
    )
    perfect_numbers = []
    number_to_test = 1
    while len(perfect_numbers) < input_int:
        if number_is_perfect(number_to_test):
            perfect_numbers.append(number_to_test)
        number_to_test += 1
    print(f'Perfect numbers are {perfect_numbers}')


def ex_4():
    text = input('Input some text:')
    import string
    # I am lazy so I am going to use the punctuation list from python
    punctuation_list = [a for a in string.punctuation]  # punctuation is a constant in string module
    punctuation_list.append('?')  # It is missing the question mark, so we add it manually
    # Making a list of all punctuations used in the text
    punctuations = [char for char in text if char in punctuation_list]
    # Removing all punctuations we found from the text
    no_punctuations_text = text
    for punctuation in punctuation_list:
        no_punctuations_text = text.replace(punctuation, '')  # Removing punctuations from text
    word_list = no_punctuations_text.strip().split(' ')  # Splitting string into list of words
    word_set = set(word_list)  # Creating set of words
    punctuation_set = set(punctuations)  # Creating set of punctuations
    print(f"All words used are {word_set}")
    print(f"All punctuations used are {punctuation_set}")
    # Counting all words and punctuations
    word_count = dict()
    punctuation_count = dict()
    for word in word_set:  # We iterate the word set because elements are unqiue
        word_count[word] = word_list.count(word)
    for punct in punctuation_set:
        punctuation_count[punct] = punctuations.count(punct)
    max_word_used = max(word_count.values())  # We find the highest number of times used for a word
    max_punct_used = max(punctuation_count.values())
    for key, value in word_count.items():  # We find the key in our dict that has the same number as max number
        if value == max_word_used:
            print(f'Word {key} was used most time, {value} total')
            break
    for key, value in punctuation_count.items():
        if value == max_punct_used:
            print(f'Punctuation {key} was used most time, {value} total')
            break


if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: ex_1,
        2: ex_2,
        3: ex_3_1,
        4: ex_3_2,
        5: ex_4,
    }
    while True:
        # Printing after every exercise execution again
        print('Type the number of the exercise to test:')
        print('1: Palindrome exercise')
        print('2: Prime number exercise')
        print('3: Perfect number exercise Pt1')
        print('4: Perfect number exercise Pt2')
        print('5: Text processing exercies')
        print('Type exit to exit the program')
        inpt = input('Exercise number: ')
        if inpt.lower() == 'exit':
            exit()
        ex_nr = int(inpt)
        exercises_map[ex_nr]()  # Executing the function at the selected number
        print('')  # Empty space for separation
