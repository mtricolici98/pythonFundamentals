# Lesson 7 - Functions

As our programs are growing more and more complex, we realize that you can't have everything run in one sequence.
Sometimes you want to access a part of the program in more than one place, and copying the code over is a major
inconvenience.

Functions allow us to do just that.

## What are functions

You already know functions, they are things that do other things.

A function is a way to declare a re-usable piece of code. That function can be later called anywhere in your program.

But what if I want to create my own function ?

In order to create a function, you must use the **def** keyword. Function declarations should always end with **():**

````python
def my_function():
# Do something cool here
````

All functions must contain a body.

If you want to create a function, but don't want it to do anything, you can use the **pass** keyword.

**pass** can be used anywhere you "have" to write code but don't want to.

````python
def function_that_does_nothing():
    pass  # I will add code later
````

## Syntax

**Functions** use the same syntax as **if** blocks and **for** loops. The code that belongs inside the function must be
indented.

## Arguments

Arguments are variables passed to the function from the function **caller**. They can be used inside the function and
are guaranteed to have a value (including **None**).

You can define your arguments by putting them inside the parentheses. See example below.

```python
def smiley_print_function(text):
    # Function that prints the text and smiley faces
    print(f" :) {text} :) ")
```

The **smiley_print_function** above will accept one argument **text**.

```python
def smiley_print_function(text, smiley_face_to_use):
    # Function that prints the text and smiley faces
    print(f" {smiley_face_to_use} {text} {smiley_face_to_use} ")
```

You can declare as many arguments as you want. Just make you provide the arguments when calling the function.

## Calling functions

There is only one main way to call a function. Using the parenthesis.

When calling a function, you must be sure that you are providing the necessary arguments. Otherwise an error will occur.

```python
def smiley_print_function(text, smiley_face_to_use):
    # Function that prints the text and smiley faces
    print(f" {smiley_face_to_use} {text} {smiley_face_to_use} ")


smiley_print_function('Hello Python', ':)')  # Prints  :) Hello Python :) 
smiley_print_function('Hello Python')  # Creates Error
```

### Returning Values

Functions can execute other functions, and can return no values or some values.

Example of a function that returns a value is the **input()** function.

It returns the value the user inputs from the keyboard.

When creating functions we can choose to return values or not.

Returning values from a function is done using the **return** keyword.

```python
def smiley_input_fn():
    user_input = input()
    return f":) {user_input}"
```

You can either return values directly, or return variables, or return None

```python
def function_that_returns_directly():
    ## Some code
    return "Some value"
```

```python
def function_that_returns_variables():
    some_variable = None
    # some calculation
    return some_variable
```

In case you want to return Nothing (**None**) you can either use **None** or just type **return**

```python
def function_that_returns_nothing():
    # some procesing
    return None


def also_function_that_returns_nothing():
    # some procesing
    return
```

### When to use return ?

You can use return whenever you like. But you must know that any code written after the return will not execute, this is
why most function return at the end.

```python

def function_with_return():
    # Some code
    return
    # Some code that won't execute
```

We can use return to our advantage in some cases. For example, if there's no point of running the rest of the code.

```python
def function_with_early_return():
    some_data = input('Give me data')
    if not some_data:
        return
    ## Do processing on some data
    return "Result"
```

In the code **above** we return immediately after we noticed that there is nothing to work with, without evaluating the
rest of the code.

Most developers consider that also to be easier on the eyes.

Let's compare this to the same function where we return at the end.

```python
def function_without_early_return():
    some_data = input('Give me data')
    if not some_data:
        result = None
    else:
        ## Do processing on some data
        result = 'Result'
    return result


## Or

def another_function_without_early_return():
    some_data = input('Give me data')
    result = None
    if some_data:
        result = 'Result'
    return result
```

### Values you can return

You can return any data type. The value returned from the function can be assigned to another variable, or be processed
directly.

````python
def my_function():
    return 'Something'


my_variable = my_function()  # Something gets assigned to my_variable

my_upper_var = my_variable.upper()  # Applying uppercase to Something

## Or

my_upper_var = my_function().upper()  # The returned variable from the function can be used directly


def another_function(some_value):
    print(some_value)


another_function(my_function())  # Function results can be passed directly as arguments to other functions
````

### All functions have a return value

It doesn't matter if you user **return** or not. All functions will return either a value or **None**

```python
def function():
    print('I didnt type any return')


variable = function()  # variable is assigned None
print(variable)  # None
```

## Keyword arguments (kwargs)

Arguments are divided in two types **positional** and **keyword** arguments.

You are already familiar with **positional** arguments. These are arguments that you must use in the same order as
requested by the function.

```python
def positional(arg1, arg2, arg3):
    pass


positional('arg1', 'arg2', 'arg3')  # Using positional arguments
```

There are cases, where you might want to pass arguments in a different order than the one requested by the function

This is where keyword arguments come to the rescue. You can provide keyword arguments by

```python
def keyword_example(arg1, arg2, arg3):
    pass


keyword_example(arg2='arg2', arg1='arg1', arg3='arg3')
```

#### How to use keyword arguments

The only rule with **Keyword** arguments is that they can be used **only after** **positional** ones, and you are **not
allowed** to use **positional** arguments after keyword arguments.

```python
def smiley_print_function(text, smiley_face_to_use):
    # Function that prints the text and smiley faces
    print(f" {smiley_face_to_use} {text} {smiley_face_to_use} ")


smiley_print_function(smiley_face_to_use=':)', text='Hello Python')  # Prints  :) Hello Python :) 
smiley_print_function(smiley_face_to_use=':)', 'Hello Python')  # Causes SyntaxError
```

## Function Defaults

There are cases when you don't want all of your arguments to be required. Maybe some are optional.

This is where defaults come in.

Defaults are defined by assigning a value to an argument

```python
def smiley_print_function(text, smiley_to_use=':)'):
    # Function that prints the text and smiley faces
    print(f" {smiley_to_use} {text} {smiley_to_use} ")


# Here I'm providing a custom smiley_to_use argument
smiley_print_function('Hello Python', ':(')  # Prints  :( Hello Python :(

# Here I'm providing not providing smiley_to_use argument, so it uses the default ':)'
smiley_print_function('Hello Python')  # Prints  :) Hello Python :) 
```

**Defaults** can only be provided after arguments without defaults.

You are **not allowed** to provide **non-default** arguments after you've provided default arguments.

#### What can be used as a default argument

Only immutable types can be used as default arguments

**Strings**, **integers**, **float**, **None**, **Bool**, **Tuple**, all can be used as default arguments.

**Dicts** and **Lists** and **Objects** should not be used as default arguments, as they are mutable. This means that it
is possible that your default argument will be changed. Which is bad.

````python
def example_mutable_default_arg(arg=list()):
    arg.append(1)
    print(arg)


example_mutable_default_arg()  # Prints [1]
example_mutable_default_arg()  # Prints [1, 1]
example_mutable_default_arg()  # Prints [1, 1, 1]
example_mutable_default_arg()  # Prints [1, 1, 1, 1]

````

As you can see above **mutable default arguments** can change the value result of a function every time the function is
executed.

[MoreExamples](https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/)

#### When are defaults applied

Defaults are applied only when the **positional** or **keyword** argument is missing. If you pass **None** as an
argument instead of a positional or keyword argument, it will prevail as the "winning" argument.

```python
def function_with_defaults(arg1='arg1', arg2='arg2'):
    print(arg1, arg2)


function_with_defaults()  # Prints: arg1 arg2
function_with_defaults(None)  # Prints: None arg2
function_with_defaults(None, None)  # Prints: None None
```

Passing None to the function will override the default value, and will be considered as an argument.

#### None as default argument

None is often used as a default argument, because it tells the function, that no value was supplied, or that the
programmer didn't want to supply that value.

It is useful when initializing mutable variables to use with the function.

````python
def do_user_action(some_value, user=None):
    if not user:
        user = SYSTEM_USER
    # Do stuff with some_value and user
````

In the example above, we have a function that needs to receive a user as an argument. But allows the user to be None,
and will use the System user as a **fallback**.

Fallbacks are commonly used in software engineering, they provide an alternative in case something goes wrong.

Another example

```python
def insert_row_in_database(info_to_insert, database_connection=None):
    if not database_connection:
        # No existing database connection is provided, making a new one
        database_connection = initialize_new_database_connection()
    database_connection.insert(info_to_insert)
```

### Typed arguments

Similar how you can suggest the type of a variable, you can suggest the type of an argument, in the same manner.

```python
def add_two_numbers(a: int, b: int):
    return a + b


add_two_numbers('New', 'York')  # returns 'NewYork'
add_two_numbers(20, 30)  # returns 50
```

Typing arguments helps you (the programmer) or other of your colleagues to know exactly what the function expects,
without needing to look into the code and what it does.

## Importing functions from other files

Python allows importing values, functions and other things from different files.

This is best explained with an example.

Let's create a file:

functions.py

````python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')
````

In the file above we have a function, that we may want to use across different python files.

In python, there are two ways to import stuff (objects, variables, functions):

1. Importing the entire module using the **import** keyword
2. Importing the specific function/object/variable, using **from** _module_ **import** _function_name_

To continue let's create another file.

program.py (or whatever you like)

Example: Importing the entire module

```python
# program.py

import functions

functions.smiley_function('I am running a function from a different file')
```

The above code, will import the entire functions.py module into the current python script.

Example 2: Importing the function alone

```python
# program.py

from functions import smiley_function

smiley_function('I am running a function from a different file')
```

The example above only imports the **smiley_function** from the functions **module**

### Importing multiple functions from the same module.

If we want to add more functions in our **functions.py** file, we can easily do so.

```python
# functions.py
def smiley_print_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


def number_input_function():
    user_inpt = input('Please type a whole number: ')
    if user_inpt.isnumeric():
        return int(user_inpt)
    else:
        return smiley_print_function('I asked for a whole number')
```

And if we want to import more than one function using the **from ... import** syntax, we can do so by separating the
function names by comma (**,**).

```python
# program.py
from functions import smiley_print_function, number_input_function
```

### What is a module

Modules are simply **.py** files that can be imported into other **.py** files. We can look at them as libraries that
contains various functions we want to use in multiple places (programs/scripts)

You can have an entire folder that acts as a module. This is what is called a package.

As our project will grow more and more complex, we will start seeing submodules/packages more often.

## Declaring a package

As I said, a package is a folder that contains multiple **.py** files or other packages.

Let's say we have a structure like below

````
Project
|---project_utils
|   |---__init__.py
|   |---database_utils.py
|   |---datetime_utils.py
|---services
|   |---__init__.py
|   |---database_service.py
|   |---file_utils.py
|---main.py
````

Our program logic may be in **main.py**

Inside **main.py** we might want to access some of our utils and services

````python
# main.py

from project_utils.database_utils import process_query_result
from services.database_service import query_database


def main():
    query_result = query_database(...)
    result_list = process_query_resullt(query_result)
````

## The __ init __ file

The init file is an optional (as of python 3.6) file that declares that the folder is a python module.

The init files are mostly used to provide "shortcuts" to functions or sub-modules inside our module

For example:

```python
# Project.services.__init__.py
# Importing functions from database_service module into the root of the package for easier access
from database_service import query_database, create_databse, create_table, delete_table, delete_database

```

Now, because our __init__ file imports functions from the **database_service**, we can access them directly from the
**services** module.

```python
# Now we can do this, because the services package already imports the functions from the database_service
from services import query_database
# Instead of this
from services.database_service import query_database
```

The init file can also be used to initialize some common logic in the package.

For example, in our services' init file we might want to create check if a folder to store program files is available
and create it if it isn't, we might also establish a database connection

```python
# Project.services.__init__.py

from database_service import *
from file_utils import *

# Doing initialization logic for our package

# Checking if database exists
if not database_exists('DEFAULT_DATABASE'):
    # creating database
    create_database('DEFAULT_DATABASE')

# Checking if folder for files exists
if not folder_exists('program_files'):
    # Creating folder
    create_folder('program_files')
```

You must be careful with the initialization logic for a package, because it will run every time the package is imported.

### name == main

Remember ``if __name__ == __main__: `` ?

Well, here is where it comes in as very important.

If our functions.py file has any code that runs inside the script. It will also be evaluated during the import.

```python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


smiley_function('Testing my function')
```

If we now import the **functions** module, the smiley_function **call** inside the module will be executed.

```python
import functions  # Will print ':) Testing my function'
```

In order to fix this, we use ``__name__ == '__main__'``

This will check, that the code is evaluated not as part of an import but as part of the script execution.

````python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


if __name__ == '__main__':
    smiley_function('Testing my function')
````

Now if we import the functions' module, the **smiley_function** inside **functions** module will not be executed.

But if we run the functions.py program, it will still display **':) Testing my function'**

### Importing multiple functions/values with same name

Say you have 2 functions in different packages that have the same name

functions.py

```python
def factorial(nr):
    pass  # Implement factorial here
```

main.py

```python
from functions import factorial
from math import factorial
```

Above we have imported 2 functions with the name factorial. This means that only the lower function will be used.

If you want to use both functions separately you can give the function a nickname. Using the keyword **as**

```python
from functions import factorial as my_factorial
from math import factorial as math_factorial
```

### Don't worry about imports yet

Imports are very important in working with small to large programs, but you don't have to worry, because most of the
time, your IDE will help you with them.
