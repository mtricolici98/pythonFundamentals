# Homework

## Guidelines

Today's homework should be all contained inside one package.

If you have common logic, please include it inside a separate module, so you can reuse that common logic.

Have a **main.py** file that will be responsible for testing all your code.

For each exercise have a testing function inside your **main.py**

When the user runs **main.py** he should be prompted with a message asking: _Which exercise would you like to test_

Each variant should contain a short explanation of what the exercise is about.

You can easily achieve this by doing as in the example below:

```python
def ex_1():
    pass


def ex_2():
    pass


if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: ex_1,
        2: ex_2
    }
    print('Type the number of the exercise to test:')
    print('1: Palindrome exercise')
    print('2: Prime number exercise')
    ex_nr = int(input('Exercise number: '))
    exercises_map[ex_nr]()  # Executing the function at the selected number
```

After the user selects an exercises, go through the testing

## Exercises

### Ex 1

Write a Python function that checks whether a passed string is palindrome or not. The function should return True or
False.

_A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run._

Test your code by providing various inputs, and providing relevant outputs.

### Ex 2

Write a Python function that takes a number as a parameter and check the number is prime or not

_A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and
itself._

### Ex 3

Write a Python function to check whether a number is perfect or not.

Write another function that will find **n** perfect numbers, and return a list of those **n** perfect numbers.

Use input from console to define **n**.

_In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that
is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a
perfect number is a number that is half the sum of all of its positive divisors (including itself)._

Example:
6 is a perfect number because 1 + 2 + 3 = 6

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14

### Ex 4

Write a program to return the information about text of any length input from the console.

The program should print out:

* All the words used in the text. (A set of all the words)
* All the punctuation marks used in the text. (Any character that's not a letter or a number is a punctuation except for **space**.)
* Count of the most commonly used word
* Count of the most commonly used punctuation

