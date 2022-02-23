# Homework note 1:

As you have seen, **open()** works with files that are in the same folder as the .py file.

When you want to read files using **open()** you should either provide the name of the file: example _my_file.txt_ (for
a file that is in the same folder as the .py file you are executing)

```python
file = open('my_file.txt')
```

Or you can provide the full path to file: example _'C:\\files\\new_file.txt'_ Use backslash \ to escape the backlash in
the file path.

### How to get the path of a file ?

#### In pycharm

![img.png](img.png)

Then

![img_1.png](img_1.png)

#### In windows

![img_2.png](img_2.png)

Then

![img_3.png](img_3.png)

This will give you the path to the folder.

Add \new_file.txt to it, and you have your full file path.

In my example it's C:\\files\\new_file.txt

# Exercises

## Exercise 1

Create a python program or function that will let the user type anything in a console, and the program should tell the
user if what he typed is an integer, a float or a string.

Hint: Try to convert to integer, if that doesn't work, try to convert to float, if that doesn't work, it means that the
input is a string.

## Exercise 2

Create a python program that will create a file with the name input from console.

## Exercise 3

Create a python program that will open the file _ex_2_file.txt_ [find it here](files/ex_2_file.txt) and print out it's
content.

## Exercise 4

Create a python program that will read the **name** of a file from the console.

Then, create a file with the **file name** input from the console. Then ask the user to type any text.

The text input by the user should be then added to the file.

Then print the text input by the user from the file.

## Exercise 5

Create a program where the user has 2 options.

* List all dishes
    * Prints out all dishes from a file
* Add dish
    * Adds a dish and saves it to the file

The program should save the list of dishes to a file. (Use JSON to store the information inside the file)

If the user closes the program and opens it again. List all dishes should print out the previously saved list of dishes.

Use [this](../class_examples/exemplu_program_json_files/main.py) to gide yourself.

# Extra homework - if you are bored

## Extra exercise 1

Create a Python program that takes a text file name (or path) as input and returns the number of words of a given text
file.

_You can use this file to test_: [find it here](files/ex_2_file.txt) or make your text file with a paragraph from your
favourite book.

## Extra exercise 2

Create a Python program that takes a text file name (or path) as input and prints out the count of each character in the
text.

_You can use this file to test_: [find it here](files/ex_2_file.txt) or make your text file with a paragraph from your
favourite book.

## Extra exercise 3

Create a Python program that takes a text file name (or path) as input and prints out the line in the text file that has
the highest number of words.

Use this file [file](files/extra_ex_3_file.txt)
