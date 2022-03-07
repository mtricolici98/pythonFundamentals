# Why python is cool

Python is considered a very versatile language, and that's for good reason.

You may have already noticed that python allows you to do many things, as long as you follow the syntax.

A good example of this, is unlimited or unspecified arguments:

````python
def unlimited_args_function(*args):
    print(args)
````

This method is not possible in many other languages, but in python it's not only possible, but commonly used.

## Re-learning what we learned

In programming there always multiple ways to solve something.

It is important for us to understand those "new" ways we discover, understand why they are bad or good, and find a way
to apply them going forward.

They say you live you learn, in programming you learn every single day.

## kwargs

Kwargs (or keywords arguments), can be packed similarely to how we pack arguments, but instead of using the * sign, we
use two of them.

`**kwargs` - will pack all of the items into a dict.

```python
def packing_function(*args, **kwargs):
    print(f"Args are:", args)
    print(f"Kwargs are:", kwargs)


packing_function(1, 2, 3, one=1, two=2, three=3)
# Args are: (1, 2, 3)
# Kwargs are: {'one': 1, 'two': 2, 'three': 3}

```

Because our kwargs is adict, we can process elements from it manually.

```python

def example(*args, **kwargs):
    if 'one' in kwargs:
        print('One is ', kwargs['one'])


example(one=1, two=2, three=3)
# Args are: (1, 2, 3)
# Kwargs are: {'one': 1, 'two': 2, 'three': 3}

```

The packing of both args and kwargs is (as you will see) very useful for when we don't know what arguments we may have,
or need to pass somewhere else.

For example, before now, we declared `__init__` functions like this.

```python
class Base:

    def __init__(self, a, b, c, d, e):
        self.a, self.b, self.c, self.d, self.e = a, b, c, d, e


class Derived(Base):

    def __init__(self, other, another, a, b, c, d, e):
        super().__init__(a, b, c, d, e)
        self.other, self.another = other, another


example = Derived(1, 2, 3, 4, 5, 6, 7)

```

But what if I'm very lazy, and I don't want to always have to write that many arguments, especially when I just need to
pass them to the next function, and then I don't need them anymore.

We can do this little trick in our derived class.

````python
class Base:

    def __init__(self, a, b, c, d, e):
        self.a, self.b, self.c, self.d, self.e = a, b, c, d, e


class Derived(Base):

    def __init__(self, other, another, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.other, self.another = other, another


# Works the same way.
example = Derived(1, 2, 3, 4, 5, 6, 7)
````

Now, I don't care what arguments my Base class has, I will pass all extra arguments to the Base class, and will let it
handle them.

## Functions

Yes, here we are again, back to talking about functions. But why ?

Functions are the way we "declare" a set of instructions. And it's also the way in which we separate our logic into
easily maintainable, reusable and functional parts.

Today I'm going to open your eyes to an interesting fact. Functions are just variables in python. They have logic
inside, but in python, everything can be a variable.

This is the reason why we can have 2 functions with the same name, where the second one is overwritten.

But how do I use it ?

## High order functions

Functions can be passed around as variables, arguments, and other.

This allows us to create functions like this:

```python
def print_element(el):
    print(el)


def apply_function_on_list(funct, list_of_elements):
    for el in list_of_elements:
        funct(el)  # Call the function from the arguments


my_list = [1, 2, 3, 4]
apply_function_on_list(print_element, my_list)  # Passaing print element function as argument
```

Because the **apply_function_on_list** function can take a functions an argument, it is considered a **high order
function**.

_A higher order function is a function that takes a function as an argument, or returns a function_

This has multiple applications in python, and is actually integrated in a lot of built-in functions.

For example, the **map** function. The map function does exactly what we did above.

````python
my_list = [1, 2, 3, 4]
map(print, my_list)  # Applies the print function to each element of my_list
````

Another example, is using the map function to get new results.

```python
def power_2(el):
    return el ** 2


list_of_els = [1, 2, 3, 4, 5]
pow_list = map(power_2, list_of_els)
print(pow_list)
# <map object at 0x000001BFD2DDDDE0>
print(list(pow_list))
# [1, 4, 9, 16, 25]
```

But wait, why did I just convert my pow_list to list again ?

This is because a map function returns a map (**iterable**) object, that acts as a **generator**, instead of processing
the entire list ahead of time. [More about them here](#what-are-iterables-and-generators)

### Sorted, Min, Max

Sorted is a function that we are already familiar with, it will return a sorted list of elements from a collection of
elements.

So are the functions min and max

What you may have not known, is that sorted, min and max can take another argument (called key) as an argument.

The key argument is an argument that specifies what value we are comparing from the element, and the key argument is
always a function.

Example, of using sorted, min and max functions with a dict:

```python
def get_age_from_dict(el):
    return el['age']


users = [
    dict(name='User1', age=42),
    dict(name='User2', age=24),
    dict(name='User3', age=32),
    dict(name='User4', age=12),
]

# We pass the function (we dont call the function ourselves, sorted will do it)
print(sorted(users, key=get_age_from_dict))
# [{'name': 'User4', 'age': 12},
# {'name': 'User2', 'age': 24},
# {'name': 'User3', 'age': 32},
# {'name': 'User1', 'age': 42}]
print(max(users, key=get_age_from_dict))
# {'name': 'User1', 'age': 42}
print(min(users, key=get_age_from_dict))
# {'name': 'User4', 'age': 12}
```

As you can see, we created a function to extract the value we are interested in when sorting. This is very useful, as we
can work with dicts and don't need to create custom classes with the `__lt__, __gt__, __eq__` methods in order to use
sorted.

This also works for objects, or any other situation where we need to work with values indirectly

````python
class ExampleObject:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Obj val {self.val}"


def get_val_from_object(obj):
    return obj.val


obj_list = [ExampleObject(5), ExampleObject(2), ExampleObject(-1)]

print(sorted(obj_list, key=get_val_from_object))
# [Obj val -1, Obj val 2, Obj val 5]
````

But do I really need to declare a function every time I need to do this ?

The answer is, not really. It depends on what processing you need to do to get that value.

If you need to make some custom logic, and have many lines of code, you will probably need a function.

But if you just need to return a single value quickly, there is an alternative. That alternative is **lambda functions**

## Lambda functions

Lambda functions is a way to quickly create one use functions.

What do I mean by quickly ? And what do I mean by one use ?

Lambda functions are functions that are not permanently registered in our programs. They are created "when necessary",
so they are not defined using the **def** keyword.

At the same time, lambda functions are somewhat limited in what they can do.

Lambda functions do one thing well, and that's return a single value.

```python
def power_2(el):
    return el ** 2


power_2_lambda = lambda el: el ** 2

print(power_2(2))
# 4
print(power_2_lambda(2))
# 4

# Using both examples on our map function.
print(list(map(power_2, [1, 2, 3, 4])))
# 1, 4, 9, 16
print(list(map(power_2_lambda, [1, 2, 3, 4])))
# 1, 4, 9, 16
```

As we can see, both the lambda and the power_2 functions work the same way, and in fact the power_2_lambda example is a
full function.

Lambda functions are declared in the following way:

`lambda args: value_to_return`

**lambda** is of course, the keyword to start defining a lambda function.

**args** are the arguments of the function.

**value_to_return** is anything you want to return from that function.

Lambda functions don't specify the **return** statement, but they always return what is after the colon (**:**).

You can have as many arguments as you want in a lambda function, and they also support default values.

Let's look at more examples.

```python
print_lambda = lambda n: print(n)
sum_lambda = lambda a, b: a + b
max_lambda = lambda a, b: a if a > b else b
sum_sub = lambda a, b: (a - b, a + b)

print_lambda('Hey, im printing from lambda function')
# Hey, im printing from lambda function
sum_result = sum_lambda(10, 24)
print(sum_result)
# 34
max_result = max_lambda(10, 5)
print(max_result)
# 10

sum, sub = sum_sub(10, 5)
print(sum, sub)
# 5 15

```

As you can see, lambda functions allow us to quickly create functions. But the best reason lambda functions are useful,
is that we can define them directly when we pass an argument.

Let's do the previous examples but now using lambda functions.

```python

class ExampleObject:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Obj val {self.val}"


obj_list = [ExampleObject(5), ExampleObject(2), ExampleObject(-1)]

print(sorted(obj_list, key=lambda el: el.val))
# [Obj val -1, Obj val 2, Obj val 5]


users = [
    dict(name='User1', age=42),
    dict(name='User2', age=24),
    dict(name='User3', age=32),
    dict(name='User4', age=12),
]

# We pass the function (we dont call the function ourselves, sorted will do it)
print(sorted(users, key=lambda el: el['age']))
# [{'name': 'User4', 'age': 12},
# {'name': 'User2', 'age': 24},
# {'name': 'User3', 'age': 32},
# {'name': 'User1', 'age': 42}]
user_names = map(lambda el: el['name'], users)
print(list(user_names))
# ['User1', 'User2', 'User3', 'User4']
```

The fact that we can quickly use those lambda functions when calling another function, is the number one reason why
**lambda is cool**.

Since we don't need to declare separate functions for such simple operations.

It's important to note that lambda functions are only useful for single operations, so you can't have multiple lines of
code.

## What are iterables and generators

Now, back to the iterables.

### Iterables

An iterable object is any object that can be iterated using the **for in** syntax.

An iterable object is not necessarily a list of collection. An iterable object can create new results as it goes on,
this is done a lot of time in order to save resources (memory).

Iterables are described by having the `__iter__` method (that returns the iterator object), and the `__next__` method
that provides the next value in our iteration.

Let me create an iterable random number generator

````python
import random


class iterable_random():

    def __init__(self, numbers):
        self.numbers = numbers
        self.curr_number = 0

    def __iter__(self):
        # Initialize our iterator
        # Done when for el in our_iterator is called
        self.curr_number = 0
        return self  # (this object is the iterable)

    def __next__(self):
        if self.curr_number >= self.numbers:
            # StopIteration exception tells python we are done iterating this object
            raise StopIteration()
        self.curr_number += 1
        # Retur new value from our iterator
        return random.randint(1, 100)


for a in iterable_random(10):
    print(a)
````

This class above, will give me a new random number on each iteration, that's to say, it will generate a new number every
iteration.

As you can see above, I have added a limit to our random number generator.

Additionally, it is possible to get only one value out of an iterable.

This can be achieved using the **next** function. The next function will ask only for the next item in the iterable.

````python
import random


class random_number_generator:

    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end

    def __next__(self):
        return random.randint(self.start, self.end)


rng = random_number_generator(0, 1000)
random_nr = next(rng)
print(random_nr)
# 77
another_random_nr = next(rng)
print(another_random_nr)
# 964
````

Because we did not provide the `__iter__` method, the generator above is not an iterator, so we cannot use the **for
in** syntax to iterate its values.

### Generators

Generators have one simple purpose, is to give us one values at a time.

Consider the following example, you have a very big source of data, and you need to process each of that item.

Let's consider that this source of data is a file, where each row is an element we need to process.

If we load the entire file data in the computer memory, we will have a lot of memory usage, we don't want that.

Generators (also called lazy iterators) allow us to give each row of the data to the necessary iterative block when it
needs it.

### The yield keyword.

**yield** keyword is very similar in function to the return keyword, in the sense that it returns a value from a
function.

However, a function can have multiple yield statements, and each of it will be executed, that is to say, the function
doesn't exit when it encounters a yield, it comes back to that function.

Let's show you an example

````python
def yield_example():
    print('Enter function')
    yield 1
    print('Back here')
    yield 2


for value in yield_example():
    print(value)
# Enter function
# 1
# Back here
# 2
````

The **yield** keyword transforms our function into a generator, but besides giving us a new value, it also is capable of
running other code (similar to how the `__next__` methods does).

```python
def yield_example():
    print('Enter function')
    yield 1
    print('Back here')
    yield 2


print(list(yield_example()))
# Enter function
# Back here
# [1, 2]
```

Random number generator example:

```python
import random


def random_nr_generator(from_number, to_number, numbers):
    for a in range(numbers):
        yield random.randint(from_number, to_number)


for a in random_nr_generator(0, 10, 3):
    print(a)
# 8
# 4 
# 5
```

### Using generators to process big amount of data.

Let's say we want to work with a large file, that has 100000+ rows.

If we load that entire file into our memory, we will use a lot of it.

We can create a generator, to give us each line, one by one.

```python
import string


def lines_from_file_generator(file):
    file_ended = False
    while not file_ended:
        line = file.readline()
        if not line:
            file_ended = True
        yield line


def count_characters_in_line(line: str):
    char_count = 0
    for el in string.ascii_letters:
        char_count += line.count(el)
    return char_count


with open('very_big_file.txt', 'r') as file:
    for line in lines_from_file_generator(file):
        print(count_characters_in_line(line))
```

in the example above, if we used file.readlines() or file.read() we would load the entire file data into our computer
memory.

This generator, allows us to easily process them line by line.

## Decorators

We already learned about decorators, we now know that hey change the behaviour of functions and methods, by wrapping
around them.

Now let's take a look at how they work.

```python
def my_first_decorator(func):
    print('Inside decorator')

    # We declare a function inside our decorator function
    def wrapped_func():
        print('Before funct')
        func()
        print('After func')

    # We return a new function
    return wrapped_func
```

Let's take a look at what happens here.

We declare our decorator function, by defining a simple function, that takes another function (func) as its argument.

The func argument is required and is in fact the function that the decorator is applied over.

Inside our decorator function, we declared a new function. It's called a wrapper function.

That wrapper function is the one that executes something before, and after our func argument (which is any function we
want to decorate)

We then return the wrapped function, by doing this we basically return a new function that uses the decorated function.

```python
def my_first_decorator(func):
    print('Inside decorator')

    # We declare a function inside our decorator function
    def wrapped_func():
        print('Before funct')
        func()
        print('After func')

    # We return a new function
    return wrapped_func


@my_first_decorator
def simple_function():
    print('Im the simple function')


print('!!!!Before call!!!')
simple_function()
# Inside decorator
# Before funct
# Im the simple function
# After func


```

Above we see how this decorator works. The wrapped_func is the new function we run when accessing simple_function().

This wrapped func can do whatever we imagine.

Let's first learn how to pass our arguments to the decorated functions.

````python
def printer_decorator(funct):
    # Processing args for our function
    def wrapper_function(*args, **kwargs):
        # Passing arguments back to our function.
        value_returned = funct(*args, **kwargs)
        print(value_returned)
        return value_returned

    return wrapper_function


@printer_decorator
def list_sum(list_of_elements):
    return sum(list_of_elements)


# We don't print anything here ourselves, our printer decorator will do it for us.
result = list_sum([2, 5, 8])
# 15
print(result)
# 15
````

The arguments we want to pass to our inner function (decorated function) should always be packed into args and kwargs.

`**kwargs` are the keyword arguments, and similarly to how `*args` are packed for positional arguments, keyword
arguments are packed into `**kwargs`.

We can pass additional arguments to our decorator functions.

```python
def repeater_decorator(times_to_repeat):
    # Declaring another inner function
    def inner(func):
        # Declaring wrapper func
        def wrapper_func(*args, **kwargs):
            results = []
            for a in range(times_to_repeat):
                results.append(func(*args, **kwargs))
            return results

        return wrapper_func

    return inner


@repeater_decorator(times_to_repeat=5)
def add_numbers(a, b):
    return a + b


print(add_numbers(10, 5))
# [15, 15, 15, 15, 15]

```

Decorators can get pretty complex, but why use them ?

Decorators for a long time had been a way to reliably do the same thing with different functions, that is to modify an
unknown external function, in a way that does something we want it to do.

As per usual, let's wrap up by creating a timer decorator function.

```python
import time


def timer(func):
    def wrapper(*args, **kwargs):
        startat = time.time()
        result = func(*args, **kwargs)
        time_elapesd = time.time() - startat
        print(f'Func {func.__name__} took {time_elapesd} seconds')
        return result

    return wrapper


@timer
def time_consuming_function():
    time.sleep(1)
    print('Done')


time_consuming_function()
# Done
# Func time_consuming_function took 1.0104775428771973 seconds
```

And another useful decorator

```python
import json


def result_as_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@result_as_json
def some_function():
    return dict(name='Username', value=12)


json_result = some_function()
print(type(json_result))
# <class 'str'>
print(json_result)
# {"name": "Username", "value": 12}
```

Where I would use such a decorator ?

I could use it anywhere I know that the result of a function should always be a JSON.

This way, I wouldn't need to do the conversion in each of those functions.

Now you know how to create your own decorators.