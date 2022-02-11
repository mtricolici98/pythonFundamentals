# Lesson Three

Last time, we've worked on understanding the basic data types and operations we can do with them.

Today we will work with them some more but will make them more intractable.

## Processing user input

On our first lesson we discovered the **input()** function.

This function allows us (the programmer) interact with user and take input from him.

```python
user_string = input()
print(user_string)
```

The code above will wait for the user to type something and will print back (echo) the user input back to the user.

One thing that I didn't explain, is that **input** can also take a **string** as an argument.

````python
prompted_string = input('Type something:')
print(prompted_string)
````

This argument will not affect the value of **prompted_string** but will show a prompt to the user. If you run the
example above, you will see a result similar to the one below. After the user types 'Something', the system prints '
Something'.

```
Type something:>? Something
Something
```

### The type of our input

All the results from the **input()** function will be **string**. Even if the user types in a number.

A question may arise. What if I want to do mathematical operations with user input ?

Here's where **Type casting** comes in.

## Type casting

Casting is the process of "adapting" a value to another data type.

it is achieved with base data types by calling their type function.

```python
str_to_int = int('10')  # 10
str_to_float = float('5.5')  # 5.5
str_to_int_2 = int('5.5')  ## Results in error
float_to_int = int(4.4)  # Result will floor to 4
float_to_int_2 = int(4.9)  # Result will floor to 4
float_to_string = str(3.339)  # '3.339'
```

Booleans casting is a different story. Boolean false in other data types usually indicative of "absence of a value".

In short, if a value is absent or equals to 0, its boolean value will be false.

````python
bool('Some') is True  # True
bool('') is False  # True
bool(0) is True  # False
bool(100) is True  # True
bool(0.0) is False  # True
bool(None) is False  # True
````

Type casting allows us to convert various data types easily, so we can later perform operations.

## Putting it all together

### Let's start simple

#### A program that will calculate the area of a rectangle

````python
if __name__ == '__main__':
    length = float(input('Length:'))
    width = float(input('Width:'))
    area = length * width
    print(f'Area of the rectangle is {area}')
````

#### A program that will apply the Pythagorean theorem

Pythagorean theorem tells us that a^2 + b^2 = c^2. Which means that c = sqrt(a^2 + b^2)

sqrt - Square Root

^ - Power

If we lay this down in code, we get a program like the one below.

````python
import math

if __name__ == '__main__':
    a = float(input('a:'))
    b = float(input('b:'))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f'Value of C is {c}')
````

For this small program, we are using the square root (**sqrt**) function from the math library.

The **math** library is a built-in library, which means that it's part of python.

## The elephant in the room. The IF statement

**If** statements are one of the main pillars of programming. They are what separates Computers from Calculators, the
ability to branch the logic based on a condition.

IF Statements are constructed in the following way

````
if condition:
    # Body
elif other_condition:
    # Body 2
else: 
    # Body 3
````

What they allow us to do, is conditionally execute code, that is to say, that we will only execute code when certain
conditions are met.

### The if

**if** is used to start a conditional block. It should always be followed by a condition that will yield boolean or
truthy expressions.

### The elif

**elif** allows us to provide additional conditions, if the first one is not met

### The else

**else** is used to handle the case when none of the above if conditions is met. It's not required to have an **else**
after every **if**.

### How it works

If statements work in a "sequential way", and a condition is met when the value of the condition is True.

Example:

```python
age = int(input('Your age:'))
if age >= 18:
    print('You are allowed to drink alcohol')
else:
    print('You are not allowed to drink alcohol')
```

The above example, uses the comparison for **age**, this way, only when the condition is True (age is >= 18) the program
will print 'You are allowed to drink alcohol'.

If the first condition is not met, the statement in the else block will be executed.

There can only be one **else** per if statement.

There can also be an unlimited number of elif statements, example below:

```python
age = int(input())
if 0 <= age < 4:
    print('You are a baby')
elif 4 <= age < 7:
    print('You should be in kindergarden')
elif 7 <= age < 12:
    print('You should be in school')
elif 12 <= age < 18:
    print('You are a teenager')
elif 18 <= age < 55:
    print('You are an adult')
else:
    print('You are elderly')
```

If statements can also be nested

```python
a = int(input())
if a == 69:
    print('You guessed it')
else:
    if a < 69:
        print('Higher')
    else:
        print('Lower')
```

As mentioned previously, if statements execute in the order they are met, thus if we have 2 blocks, and both are true,
only the first True block will be executed, example below.

````python
if True:
    print('First block')
elif True:
    print('Second Block')
else:
    print('Third Block')
````

The second block will never be executed, because the first one completes the if statement.

The **else** block only executes if none of the previous **if**/**elif** statements have been completed.

### Truthy expressions

As mentioned in the previous lesson, all data types can be expressed as booleans.

For example: **None** will be interpreted as **False** as indication of absence of a value and **'I am a string'** will
be interpreted as **True**. Such expressions are known as Truthy.

As an example.

```python
text = input('Type anything:')
if text:
    print('Good job')
else:
    print('You fool')
```

In the example above, we never compared text to anything, we never asked the computer to check if the value is empty or
not. But if we run the program and type anything in the console, it will say **'Good Job'** and if we just hit enter it
will say **'You Fool'**. This is because python interprets non-empty strings as **Truthy**.

Other examples of truthy expressions are:

* Non-zero numbers (both **int** and **float**)
* Non-empty collections (**list**, **tuple**) (Will learn during our next lesson)

## Ternary if expressions

Sometimes you want to have a simple if/else block, but don't want to use much space. You can use inline if statements.

It's most useful when one value depends on another value. For example:
Discount should be 20% if user is a student

One way to write this would be

```python
user_is_student = input()
discount = 0
if user_is_student:
    discount = 20
```

Inline **if** expressions allow us to write the same logic in a "simpler" way.

```python
user_is_student = input()
discount = 20 if user_is_student else 0
```

Inline if expressions have the following syntax:

_value_if_true_ **if** _condition_ **else** _value_if_false_

It is also possible to have nested if expressions, but it's generally not advised

````python
user_is_student = input()
user_is_elder = input()
discount = 20 if user_is_student else 40 if user_is_elder else 0 
````

which is the same as

```python
user_is_student = input()
user_is_elder = input()
discount = 0
if user_is_student:
    discount = 20
elif user_is_elder:
    discount = 40
```

Another way to use inline if expressions is when you are not sure if the first variable has a value.

```python
maybe_empty_var = None
fallback_var = 'Fallback'
result = maybe_empty_var if maybe_empty_var else fallback_var
```

This checks if maybe_empty_var is truthy, and if it is, it will take it's value, otherwise, it will use the fallback
var.

Another way of doing the process above is through the **or** operator

```python
default_discount = 5
custom_discount = None

discount = custom_discount or default_discount  # 5
custom_discount = 10
discount = custom_discount or default_discount  # 10
```

The or will evaluate default_discount only if there is no custom discount (warning: if custom_discount is **0**
default_discount will be used.)

In order to avoid such issues we can use ternary if:

```python

default_discount = 5
custom_discount = 0
discount = custom_discount if custom_discount is not None else default_discount
# OR
discount = default_discount if custom_discount is None else custom_discount
```

## Understanding \_\_name\_\_ == '\_\_main\_\_'

You've encountered it in various places, but why is it needed.

Python code is executed by going through the script file line by line, but sometimes, you need to process the file
without executing things, for example, when you import from another file (module).

The ```if __name__ == '__main__'``` checks if the file is executed directly (by running the script) or if it's being
processed as part of an import.

It's not required to have it in your program, but it's good practice having it.

## String formatting

Whether we like it or not, we will work a lot with strings in programming. We use strings a lot, because it's an
efficient way of talking both to the user and to the programmer.

It is important to know how to format your strings. Here's what you need to know.

String formatting, is the process of inserting values and variables into pre-defined text.

Similar how we have previously done the Hello example.

```python
name = input('Your name')
print('Hello, ' + name)
```

However, what we've done above is just some string concatenation, you can easily see how this may get out of hand.

```python
name = input('Your name')
age = input('Your age')
country = input('Your country')
height = input('Your height')
print('Hello, ' + name + ' aged ' + age + ' years from ' + country + ' with a height of ' + height)
```

I agree that the process above is tiresome and we should probably find a better way to do it. It so happens that a lot
of people thought this way too. So here is a couple of ways we can get this done in a better way.

### The old style way

```python
name = input('Your name')
age = input('Your age')
country = input('Your country')
height = input('Your height')
print('Hello, %s aged %s years from %s with a height of %s' % (name, age, country, height))
```

This process is using "placeholders" for our pieces of text represented by the **%** sign. Following the **%** sign you
can declare the type of the value you want to format.  **%s** Tells the interpreter that you intend to display a string.
Other type operators are available, here's the full list.

| Value  | Presentation Type             |
|--------|-------------------------------|
| b      | Binary integer                |
| c      | Single character              |
| d      | Decimal integer               |
| e or E | Exponential                   |
| f or F | Floating point                |
| g or G | Floating point or Exponential |
| o      | Octal integer                 |
| s      | String                        |
| x or X | Hexadecimal integer           |
| %      | Percentage                    |

It is also possible to provide full names for the values you want to represent

```python
print('%(name)s, age %(age)d' % {'name': 'Marius', 'age': 24})
```

Not all of them work for the modulus method. So here is another way to format strings.

### String .format

The modulus operation on strings described above is a bit old, so here is a newer way to do string formatiing.

```python
print("{} is {} years old".format(
    'Marius', 24
))
```

Inside a string, place a {} and it will act as the placeholder for any value you want to insert. Then use the .format
function of the string to provide the values to fill.

It is possible to specify the type and provide a name as it was possible with the % method of sting formatting.

```python
print('{:s} is {:d} years old'.format(
    'Marius',
    24
))

print('{name:s} is {age:d} years old'.format(
    name='Marius',
    age=24
))

# The example below will not work
print('{name:s} is {age:d} years old'.format(
    'Marius', 24
))
```

If you provide empty placeholders (without a name), they will be filled in the order of the arguments to the format
function. If you provide at least one placeholder with a name, you have to use names on all of them.

### F-string

The F-string were introduced to python in version 3.6 and have been ever since the best way to build and format strings.

To create an f-string you just need to put **f** in front of the string.

```python
f_string = f'I am a f-string'
```

F-strings allow inline formatting

```python
name = input()
age = input()
print(f'Hi, i am {name}, and am {age} years old')
```

F-strings support the same type formatting as % and .format()

````python
name = input()
age = input()
print(f'Hi, i am {name:s} and am {int(age):d} years old')
````

### Numbers formatting

The most used formatting trick is usually numbers formatting.

We may want to format 1.33333333 to just look like 1.3 or 1.33

```python
a = 1.3333333
print(a)
print(f'{a:0.2f}')  # 2 digits after decimal point
print(f'{a:0.1f}')  # 1 digit after decimal point
b = 1200
print(f'{b:04}')  # minimum 4 digits, fill with 0
b = 123
print(f'{b:04}')  # minimum 4 digits, fill with 0
print(f'{b:1>5}')  # minimum 5 digits, fill with 1
print(f'{b:->5}')  # minimum 5 digits, fill with '-'
c = 12.321
print(f'{c:0>5.1f}')  # minimum 5 digits, fill with 0, 1 decimal, (includes the .)
c = 123.32
print(f'{c:0>5.2f}')  # minimum 5 digits, fill with 0, 2 decimals, (includes the .)
print(f'{c:0>8.2f}')  # minimum 8 digits, fill with 0, 2 decimals, (includes the .)
```

The last 4 examples show examples of padding (adding something before the value) to make the value fit in a specific
way. Maybe we want to show the value as part of a table.

There are many more string formatting possibilities, and I encourage you to try them out yourself.

## Links

[Conditionals](https://realpython.com/python-conditional-statements/)

[String Fomratting](https://realpython.com/python-string-formatting/#which-string-formatting-method-should-you-use)

## Exercises

Throughout all the exercises, prompt the user with the proper question when using **input()** and use descriptive
**formatted** results where applicable.

1. Write a program that will ask the user for the dimensions (width, length, height) of a cuboid, and will calculate and
   print its volume Example:

```
Input: 
30
40
20
Ouput:
Volume is: 24000
```

2. Write a program that will ask the user for two numbers. The program should print out the highest number. Try to make
   it as short as possible.

```
Input: 
99
102
Ouput:
Highest number is: 102
```

3. Write a program that will ask the user his **Name**, **Age** and **Gender** then it will print one of these welcome
   messages
    1. ``Welcome Mr. (name) `` if the user is a male that is above 18 years.
    1. ``Welcome Ms. (name) `` if the user is a female that is above 18 years.
    1. ``Yo, (name) `` if the user is below 18 years old.

```
Input:
Elizabeth
95
F
Output:
Welcome Ms. Elizabeth
```

4. Write a program to read temperature from user input and display a suitable message according to temperature state
   below.
    1. Temp < 0 then 'Freezing weather'
    2. Temp 0-10 then 'Very Cold weather'
    3. Temp 10-20 then 'Cold weather'
    4. Temp 20-30 then 'Normal in Temp'
    5. Temp 30-40 then 'It's Hot'
    6. Temp >=40 then 'It's Very Hot'

```
Input:

Output:

```
