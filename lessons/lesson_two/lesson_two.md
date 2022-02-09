## Lesson two

## Data types, operations, variables

Last time we had discovered ways to declare variables, and the rules that apply to that process. Now in order to
understand better the data types we can work with and their strengths and limitations, we are going to take a closer
look at each of them.

## Recap from last lesson

Lets first try to remember what are variables, and how we declare one.

A **variable** is a reference to some data, in short, a variable is the "name" we use to access some information
somewhere in the memory.

**Variable declaration** is the process in which we let the computer know that we want to have a new variable, with a
desired name, that holds a value or no values at all.

In order to declare a variable, we should give it a name.

As we discussed last time, variable names should:

* Start with a letter
* Describe the value they are representing
* Be easy to understand and/or reference

Variable names should not:

* Start with numbers
* Contain spaces
* Contain special characters except for **_** (underscore)

## Typing

Most programming languages have the concept of a data type, and some of those languages require the programmer to
specify explicitly what data type it's representing

In Java for example, you might have to do something like this:

````java
int myNumber = 0;
````

Java, alongside many other languages, requires explicit type declaration. Which is the **int** part of the variable
declaration. This way, in Java we tell the computer that **myNumber** can only be of type **int**. Explicitly typed
programming languages require you to always define the type of the variable, and will cause errors when values of the
wrong type are used with a variable.

In Python, types are assigned to variables "implicitly", which means that the interpreter sets the type of the variable
based on its value. Thus the declaration of the variable lacks the type declaration.

```python
my_number = 0
```

## Explicit type declaration in Python

Python "supports" explicit type declarations. But compared to other languages, the type declarations are nothing but a
suggestions.

You can declare the type by specifying it with **:** (colon) after the name of the variable.

```python
my_int: int = 0  # Now the interpreter will know that this should be an int
my_int = 'String'  # The IDE will complain, but the code will run
```

# Python Base Data Types

Python has a short but very robust set of built-in unit types.

**Integer**, **String**, **Boolean**, **Float**

## Strings

Sometimes referred to as **str**

You may be already familiar with strings, since we used them in the previous lesson.

In short, strings are a list of characters, and behaves mostly like a list of characters.

Strings can be defined by including text in between single or double quotes (**' '** or **" "**). The opening quote
should be the same type as the closing one, the example below will demonstrate.

```python
valid_string = 'Valid String'
```

```python
valid_string = "Valid String"
```

```python
invalid_string = 'Invalid String"
invalid_string = "Invalid String'
```

It is also possible to initialize an empty string

```python
i_am_empty = ''
```

#### Immutability

Strings are immutable.

When a data type is immutable, this means that it can not be changed. If you create a string '
Hello', you are not allowed to change any of the letters. If you want to make all letters lowercase, you will have to
create a new string, from the old one. In the computers' memory a new **value** will be created and will **replace** the
old one

### Operations on strings

As we have previously seen, some operations are available on strings, for example you can **concatinate strings**

```python
concatenated_strings = 'First string, ' + 'Second String'
# Result will be "First string, Second String"
```

It's also possible to easily change the the case of a string.

Python provides methods, accessinble on a string to change the case, or replace characters. All with one function.

````python
my_string = 'Hello Python'
my_lowercase_string = my_string.lower()  # hello python
my_uppercase_string = my_string.upper()  # HELLO PYTHON
my_swap_case_string = my_string.swapcase()  # hELLO pYTHON
len(my_string)  # 12
spaced_string = '   I have spaces around text   '
no_space_string = spaced_string.strip()  # Remove spaces on left and right
no_left_space_string = spaced_string.rstrip()  # Remove spaces from right only
no_right_space_string = spaced_string.lstrip()  # Remove spaces from left only

new_string = 'Abba'
new_string.count('a')  # 1
new_string.count('b')  # 2
new_string.count('bb')  # 1
````

### Accessing individual characters

```python
my_str = 'Hi!'
print(my_str[0])  # H
print(my_str[1])  # i
print(my_str[2])  # !
```

This would be a great time to learn about how lists are stored in programming.

## How lists are stored

As mentioned above, a string is a list of characters. Lists are ares of memory where each individual item of a list can
be accessed by an index.

In the **string** examples above you can see that we access the indexes 0 to 2.

To access elements of a list, we need to use the square brackets **[ ]** and indicate the Index of the element in the
list.

**Indexes** always start the count with 0 so the first element is always as index 0.

### Accessing parts of a list

Taking the above example, maybe we want to only access the first two letters on the string.

In python, it's really easy to access parts of lists. Using the square brackets [ ] we can speicify the part of the list
we need.

```python
my_string = 'Some String'

some = my_string[0:4]  # Some
string = my_string[5:]  # String
another_some = my_string[:4]  # Some
```

In the example above, we can see multiple ways of accessing parts of a list.

The first way, specifies both the start and end of the list.

The second way, only specifies where to start, and will extract from that index to the end.

The third way, only specifies where to stop, and will extract from the beginning to the chosen index.

## Integers

Also known as **int**

Integers are simple. They represent natural (whole) numbers, 1, 2, 3 ... 99999. They don't allow decimal points (0.8)
but they can handle most of the arithmetical.

They are also [immutable](#Immutability)

## Floats

Floats are similar to integers, but very different. They represent real numbers, so they allow decimal points (1.3333).
More info on how floats work: [link](https://youtu.be/PZRI1IfStY0).

Most arithmetic operations are available for both floats and integers. So I will explain them.

They are also [immutable](#Immutability)

## Arithmetic operations in python

### Addition

Pretty self-explanatory.

```python
a = 1 + 2  # a = 3
```

### Subtraction

Pretty self-explanatory too.

```python
b = 4 - 1  # b = 3
```

### Multiplication

Self-explanatory as well.

```python
c = 4 * 3  # c = 12
```

### Division

During the division of 2 numbers, the result variable will always be a float.

```python
d = 4 / 3  # d = 1.333333333333
e = 4 / 2  # e = 2.0
```

### Modulus

'%' is the operator that calculates the remainder of the division of 'a' and 'b':

```python
f = 4 % 2  # f = 0
g = 4 % 3  # g = 1
h = 4 % 12  # h = 4
i = 12 % 4  # i = 0
```

The most commonly used application for modulus is to determine if a number is even or odd. If you divide everything by
2, if it has a remainder, it's odd, if it doesn't, it's even.

```python
42 % 2  # 0, even
37 % 2  # 1, odd
1 % 2  # 1, odd
0 % 2  # 0, even
```

### Exponential

The exponential operator '**' is used to raise 'a' to the power of 'b'

````python
2 ** 2  # 4
2 ** 4  # 16
3 ** 4  # 81
````

### Floor division

Floor division, is very similar to division, except it always rounds down the result to a whole number.

```python
4 / 3  # 1.333333 
4 // 3  # 1
2.9 / 1  # 2.9
2.9 // 1  # 2.0
1 / 4  # 0.25
1 // 4  # 0
```

If the floor division operation is done with all integers, the result will be an integer, if a float was present either
as 'a' or 'b', a float will be returned.

## Additional assignment operators

In python (as in many languages). It is possible to assign a new value by combining the old value with a new one. These
operators can perform arithmetical operations and work as follows.

```
+= Assign and add
-= Assign and reduce
*= Assign and muliply
/= Assign and divide
%= Assign and modulo
**= Assign and raise to power
```

With this, it is possible to easily modify the value of a variable

Example:

```python
x = 3
x += 3  # x = 6 | Equivalent to x = x + 3
x -= 3  # x = 3 | Equivalent to x = x - 3
x *= 3  # x = 9 | Equivalent to x = x * 3
x /= 2  # x = 9 | Equivalent to x = x / 3
```

This allows us to have shorter code.

## Comparison operations

Comparisons are done by one of the following operators.

* '<' less than
* '<=' less than or equal to
* '>' greater than
* '>=' greater than or equal to
* '==' equal to
* '!=' not equal to

Comparisons can be done in between either strings, or numbers. You can combine **float** and **int** but not
**int | float** and **string**.

### Comparison of numbers

Comparison can easily be done between floats and integers, they always result in [booleans](#booleans) as values

````python
1.0 > 1  # False
1.0 == 1  # True
3.4 > 3  # True
3.4 < 9.7  # True
3.40 != 3.4  # False
````

### Comparison for strings

It is also possible to compare strings.

The string comparison is done character by character. String comparisons are also case-sensitive, so 'a' is not exqual
to 'A'. The "Value" for each character is taken by their position in the [ASCII Table](https://www.asciitable.com/).

![](assets/ASCII-Table.svg.png)

As the comparison goes character by character, it will stop when it finds the first character that is not equal to the
character at the same position in the other string. If all characters are equal, the strings are equal.

```python
'a' < 'A'  # False | 97 < 65
'aa' < 'A'  # False | 97 < 65 (Second 'a' is ignored)
'ABC' < 'ABc'  # True | 65,66,67 < 65, 66, 97
'ABC' == 'ABC'  # True | 65,66,67 == 65, 66, 67
```

## Booleans

The simplest data type in the programming world.

Booleans express True or False.

```python
i_am_true = True
i_am_false = False
```

### Operations (Boolean arithmetic)

## Comparison

You can compare two booleans by using '==' - equals and '!=' not equals.

````python
True == False  # False
True != False  # True

18 < 3 == True  # True
````

## Boolean Algerba

### AND

Boolean **and**  will result in **True** only when Both booleans are **True**

```python
True and True  # True
True and False  # False
False and False  # False
```

### OR

Boolean **or** in between two booleans will result in **True** if at least one of the booleans is **True**

```python
True or False  # True
True or True  # True
False or False  # False
False or True  # True
```

Boolean operations can be chained, for example (True and False or True)

### Negation

Negation is done using the **not** keyword.

```python
a = True  # a = True
b = not a  # b = False
a is not b  # True
```

### More practical examples

```python
# Examples

age = 16
age_restricted = True

access_denied = age < 18 and age_restricted  # True and True
print(access_denied)  # True

age_restricted = False
access_denied = age < 18 and age_restricted  # True and False
print(access_denied)  # False

age_restricted = True
age = 22
access_denied = age < 18 and age_restricted  # False and True
print(access_denied)  # False
```

Same but reversed

```python
# Examples
age = 16
age_restricted = True

access_granted = age > 18 or not age_restricted  # False or False
print(access_granted)  # False

age_restricted = False
access_granted = age > 18 or not age_restricted  # False or True
print(access_granted)  # True

age_restricted = True
age = 22
access_granted = age > 18 or not age_restricted  # True or False
print(access_granted)  # True

```

## None

[None](https://www.educative.io/edpresso/what-is-the-none-keyword-in-python) (also know as 'null') indicates absence of
a value.

Variables can be initialized to None or be compared to None

```python
gender = None
```

Comparing to None is mostly done using the keyword 'is'. Although '==' also works, it is usually not recommended. We can
later see why.

```python
gender is None  # True
```

# HomeWork

1. Given the following code, what is the value of **result**

```python
result = 'Hello' * 2
```

2. Create a small program that will:
    1. Ask for user input
    2. Count the number of vowels in the user text ('a', 'e', 'i', 'o', 'u', 'y')
    3. Display the number of vowels in user text

Example

```
input: Hello
output: 2 

input: How are you ?
output: 6
```

3. Create a small program where
    1. The user inputs an email
    2. The program checks if the email ends with @gmail.com
    3. The program prints True if email ends with @gmail.com and False if it doesn't

Example

```
input: harry_potter1997@gmail.com
output: True


input: racing_drivernr1@yahoo.com
output: False
```
