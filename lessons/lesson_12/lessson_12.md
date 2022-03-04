# Additional class properties

Because python is an object-oriented langauge, classes provides a lot of various capabilities.

Classes are very versatile, and contain a lot of functionality. Most of which can be overwritten.

## Magic methods

Magic methods are methods that start with an underscore and end with an underscore. The magic methods define many of an
objects' behaviour and the way they interact with other objects.

We already know some of those magic methods, the `__init__` and `__str__` methods for example.

The first one lets us define how an object is initialized, and the other one helps us represent our object as a string.

Today we are going to discover more of what the classes have to offer.

### Comparisons magic methods

It is possible to overwrite the behaviour of an object for comparisons.

Let's define an object **Point**, which will represent a point in a 2D space. The point will have two properties: **x**
and **y**.

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'


p1 = Point(1, 2)
print(p1)
```

In order to define the object's behaviour during comparison, we need to overwrite the following magic methods.

* `__eq__` - equals to
* `__gt__` - greater than
* `__lt__` - lower than
* `__le__` - lower or equal than
* `__ge__` - greater or equal than

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __eq__(self, other):
        if type(other) != Point:
            return False
        if other.x == self.x and other.y == self.y:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            if self.y > other.y:
                return True
        return False

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


p1 = Point(1, 2)
p2 = Point(2, 2)
p3 = Point(3, 1)
print(p1 == p2)
# False
print(p1 < p2)
# True
print(p1 > p2)
# False
print(p1 > p3)
# False
print(p1 < p3)
# True
print(p1 <= p3)
# True
print(p1 <= p1)
# True
```

Now our object supports comparisons using python comparisons operators.

## More magic methods

The two magic methods we are going to define are what happens when we do arithmetic operations on with our objects.

* `__add__` - Addition
* `__sub__` - Subtraction

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __add__(self, other):
        if type(other) is not Point:
            raise Exception('Addition is only allowed for Point objects')
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) is not Point:
            raise Exception('Subtraction is only allowed for Point objects')
        return Point(self.x - other.x, self.y - other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
# Point at 3:6
print(p1 - p2)
# Point at -2:-2
p1 += p1
print(p1)
# Point at 2:4
```

Other arithmetics operators are available, but I will let you experiment yourself.

| Operator | Method     |
|----------|------------|
| +  | `__add__`      |
| -  | `__sub__`      |
| *  | `__mul__`      |
| /  | `__truediv__`  |
| // | `__floordiv__` |
| %  | `__mod__`      |
| ** | `__pow__`      |
| &  | `__and__`      |
| \ | `__or__`       |

## More magic methods.

There are a lot of magic methods. I am going to show you two more. The rest **find out what they do for yourself**.

Have you ever thought of what happens when a property of our object is accessed using the square brackets?

Example:

```python
print(p1['x'])
print(p1['y'])
# Or
p1['x'] = 2
p1['y'] = 2
```

We can overwrite the code that does that, in order to change what our class does when we want.

In order to do that, we need to overwrite the following magic methods:

* `__setitem__` - sets the item using the square brackets
* `__getitem__` - gets the item using the square brackets

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __setitem__(self, key, value):
        if key == 'x' or key == 0:
            self.x = value
        elif key == 'y' or key == 1:
            self.y = value
        else:
            raise Exception(f'Trying to set a property of Point that is not available {key}')

    def __getitem__(self, item):
        if item == 'x' or item == 0:
            return self.x
        if item == 'y' or item == 1:
            return self.y
        raise Exception(f'Trying to access an item of Point that is not available {item}')


p1 = Point(1, 2)
print(p1['x'])
# 1
print(p1['y'])
# 2
p1['x'] = 2
p1['y'] = 3
print(p1['x'])
# 2
print(p1['y'])
# 3
print(p1.x)
# 2
print(p1.y)
# 3
```

We can also forbid access or modification of our properties by overriding the `__setattr__` and `__getattr__` methods.

This is not recommended, as it will also forbid from accessing your properties even inside your objects.

Look at the example below.

```python
class ImmutablePoint:
    _locked = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._locked = True

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __setattr__(self, key, value):
        if self._locked:
            raise Exception(f'Object is immutable, modifications are not allowed')
        super().__setattr__(key, value)


p1 = ImmutablePoint(1, 2)
print(p1.x)
# 2
print(p1.y)
# 3
p1.x = 1
p1.y = 1
# Exception: Object is immutable, modifications are not allowed
```

We use the property _locked to "lock" our object against further modification.

Be careful, as we need to lock if after we set the initial values. If we lock it before, even the `__init__` function
will not be able to set the attributes of this object.

## Decorators

Decorators are functions that wrap around an existing function.

[You can read more about decorators](https://www.datacamp.com/community/tutorials/decorators-python)

We will also discuss decorators in a future lesson.

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

Decorators are applied using the @ symbol.

Python provides a couple of built-in decorators we can use to modify the behaviour of our objects.

### classmethod and staticmethod

Both **classmethod** and **staticmethod** are methods that we can declare inside our class and access them from outside
the class without needing an object instance.

This means that we can access these methods directly form the class, and we don't have access to the object instance
(self).

The difference between a staticmethod and a class method is that a **classmethod** has access to the class while a
**staticmethod** does not.

````python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


string_date = '4-3-2022'
is_valid = Date.is_date_valid(string_date)  # The staticmethod uses the class as its module.
print(is_valid)
# True
date = Date.from_string(string_date)  # The classmethod adds additional functionality to the class itself.
print(date)
# <__main__.Date object at 0x0000021F9EFCFD88>
````

### property

Property decorators allow us to have methods with custom logic, to access single properties from our objects.

````python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @property
    def full_date(self):
        return f"{self.day}-{self.month}-{self.year}"


my_date = Date(4, 3, 2022)
print(my_date.full_date)  # We access full_date without the parenthesis
# 4-3-2022
````

Properties allow us to define easy access to certain attributes of our objects and allow us to have logic inside our
properties.

The **property** decorator replaces the **full_date** transforming it from a method to a property of the object.

We can also overwrite the behaviour of our property by defining the setter functions for our properties.

```python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @property
    def full_date(self):
        return f"{self.day}-{self.month}-{self.year}"

    @full_date.setter
    def full_date(self, value):
        if Date.is_date_valid(value):
            self.day, self.month, self.year = map(int, value.split('-'))
        else:
            raise Exception('Invalid date')

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


my_date = Date(4, 3, 2022)
print(my_date.full_date)
# 4-3-2022
my_date.full_date = '5-4-2022'  # We use the setter for full_date to set the value
print(my_date.full_date)
# 5-4-2022
print(my_date.day)
# 5
print(my_date.month)
# 4
print(my_date.year)
# 2022
```

## dataclass decorator

Sometimes you need to make a simple class that is only used to represent data, with no additional functionality.

The dataclass decorator allows us to quickly do so.

The dataclass is available starting from Python 3.9, and let us quickly create classes to represent data.

To declare a dataclass, we need to declare a simple class, where we declare the properties with their types and apply
the @dataclass decorator to that class.

The dataclass decorator will automatically create the necessary `__init__` and `__str__` methods.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str


a = Person('Marius', 12, 'M')
print(a)
# Person(name='Marius', age=12, gender='M')
```

We still have the freedom to add our own methods and overwrite existing ones. But the dataclass creates the minimum
required attributes of our objects in order to easily work with it.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str

    def is_male(self):
        return self.gender.lower().startswith('m')

    def __str__(self):
        return f'{self.name} age {self.age} gender {self.gender}'


a = Person('Marius', 12, 'M')
print(a)
# Person(name='Marius', age=12, gender='M')
print(a.is_male())
# True
```

## Context managers

Context managers are a way for you to declare a wrapper around a functional block of code.

Context managers function is to take away the responsibility of managing resources from the programmer, and onto the
context manager.

Context managers are accessed using the `with` statement.

An example of a resource that can be managed, is the file (using the open function)

```python
with open('example.txt', 'w+') as file:
    file.write("Tadaaa")
```

The context manager provided by the open function will automatically close the file when the code inside it is executed,
that is to say, after python has exited the context managers' block.

You already know the rule with working with external resources (i.e. Files). Files should always be closed after you are
done with them.

What the `open` context manager does is it opens the file for you, passes the file reference to you (using the as
keyword) and then closes the file when your execution has exited the context manager.

The basic principle of a context manager is that it does something before your code runs, and then can do something
after your code inside the context manager has stopped running.

### Creating our own context managers

You may need to create a context manager, don't worry it's very easy.

Let's take a simple example. You want a context manager that calculates the time your code took to run.

You just need to declare define the `__enter__` and `__exit__` magic methods for a class.

````python
import time


class benchmark_execution:

    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_ran = end_time - self.start_time
        print(f'Code ran for {time_ran} seconds')
        return True


with benchmark_execution():
    sum = 0
    for a in range(10000):
        for b in range(10000):
            sum += a + b
    print(sum)
# 999900000000
# Code ran for 10.640141725540161 seconds
````

The exit method also allows us to handle exceptions that happened inside our code body.

The exit method should return True or False based on whether the exception (if any) was handled or not.

If the exit method returns True it will not stop the code execution (The Exception will be silenced) and all the code
outside the context manager will function as usual.

If the exit method returns False, the exception will be raised.

Example:

````python
import time


class benchmark_execution:

    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_ran = end_time - self.start_time
        print(f'Code ran for {time_ran} seconds')
        return True


with benchmark_execution():
    sum = 0
    for a in range(10000):
        for b in range(10000):
            sum += a + b
    print(sum)
    raise Exception('Some random error')
print('Heyo, im here')
# 999900000000
# Code ran for 12.248035907745361 seconds
# Heyo, im here
````

If we return False from the exit method we will see an error, and no further code will be executed.

The code inside the `__exit__` method will always be executed, regardless of exceptions.

```python
import time


class benchmark_execution:

    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_ran = end_time - self.start_time
        print(f'Code ran for {time_ran} seconds')
        return False  # Returning False to let python know it should deal with the exception


with benchmark_execution():
    sum = 0
    for a in range(10000):
        for b in range(10000):
            sum += a + b
    print(sum)
    raise Exception('Some random error')
print('Heyo, im here')
# Exception: Some random error
# 999900000000
# Code ran for 19.534482955932617 seconds
```

We can use the knowledge of the exception to handle different situations.

The 3 arguments that __exit__ provides let us know the type of the exception, the value of the exception and the
traceback.

```python
import time


class benchmark_execution:

    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_ran = end_time - self.start_time
        if not exc_val:
            print(f'Code ran for {time_ran} seconds')
            return True
        else:
            print(f'Code ran for {time_ran} before it encountered an exception.')
            return False


with benchmark_execution():
    sum = 0
    for a in range(10000):
        for b in range(10000):
            sum += a + b
    print(sum)
    raise Exception('Some error')
print('Heyo, im here')
# 999900000000
# Code ran for 11.40634560585022 before it encountered an exception.
# Traceback (most recent call last):
#   File "C:\Users\mariu\AppData\Roaming\JetBrains\PyCharm2021.3\scratches\scratch_52.py", line 29, in <module>
#     raise Exception('Some error')
# Exception: Some error
```