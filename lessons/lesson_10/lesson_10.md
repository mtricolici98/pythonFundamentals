# Objects

Last time, we discussed the **type** function.

The type function allows us to return the class of an object.

Today we will learn how to create our own classes, and in turn, how to create our own objects.

Python is an object-oriented language. In python, everything is an object.

Let's begin with what is an object:

## What are objects ?

An object is a data type that is defined as having both **state** and **behaviour**.

Object oriented-programming allows us (programmers) to create entities that reflect an abstract representations of
real-life or imaginary entities inside our code.

Let's begin with defining the properties of an object: state and behaviour.

## State

State is the property of an object to store information that "belongs" to that object.

Let's take an object as an example.

### A car

Cars are complex objects, a car can be different from another car by a combination of properties.

A car can also be composed of other objects (windows, doors, wheels, etc...)

Cars also have such properties as: color, length, number of wheels, number of doors, number of windows, etc.

A car can also have a state, for example: driving, running, stopping, stationary, parked.

All the examples listed above define the **state** of the object that is a car.

### String

Let's take a look at an object we already know.

String as we know is an object that contains a list of characters. String also has such properties as a property,
length. Which applies to it specifically.

Together, the contents and the length represent this string.

## Behaviour

Behaviour defines what you can do with that object. Behaviours are "traits" of that object that modify it's internal
state, or uses its internal state to generate new results.

We see this in many ways in python.

Behaviour of an object is defined by "methods" we can apply to those objects.

We have already practiced with using methods on objects. A **list** object for example can have its state altered by
methods such as **.append()**, **.extend()**, **.sort()**, etc.

## Methods vs Functions

In the previous weeks, we've worked with both methods and functions. But we never learned what the difference is between
a method and a function.

### Functions

Functions are pieces of programs that we can use to process information, modify and make operations with our functions'
arguments, and possibly return some results.

Functions only work with data provided by their arguments, or data from some other variable outside its scope (A global
variable for example or values imported from other files).

Example of functions: **print()**, **input()**, **sum()**, **max()**

### Methods

Methods, are also functions, but methods have access to the internal state of its object, meaning that they can process
information from inside the object the method belongs to.

A method is always part of an object, and can only be accessed using its object.

Example of methods are **my_list.append()**, **my_string.replace()**, **my_string.count()**.

Some methods can simply modify the internal value of the object, other can return results, other can do both
(example **list.pop()**).

Methods are always called in relation to an object, using the **.** (dot) to link itself to that object.

````python
my_list = []
my_list.append('element')  # Modifies the state of my_list.
my_list.count('element')  # Checks the count of occurrences inside the internal state of the list.
````

We will later learn how we can define methods.

# Classes

In programming, classes is what we call "blueprints" for our objects. Classes contain the declaration for what
properties an object can have, and what methods an object can have.

Objects are created from classes using the constructor function. Calling a class using the parenthesis will execute its
constructor function. The constructor function is what creates the instance of the object. It "constructs" the object
from the "blueprint" which is the class.

```python
my_list = list()  # Calling the constructor of the class list
```

# Defining Classes

How do we make our own classes (and eventually objects) in python ?

We already did make our own objects a while ago, when we discussed custom exceptions. Exceptions are also objects.

Defining objects is very simple.

We must use the **class** keyword to define a new type.

```python
class MyNewClass:  # Creating a new class with name MyNewClass
    pass
```

Now, we can create instances of this new type, those **instances** are our objects.

Let's create an Animal object.

````python
class Animal:
    pass


my_animal = Animal()  # Creating an instance of the Animal type
````

What can we do with this animal now ?

To answer it straight, honestly, nothing. Our animal class has no defined state and no defined behaviour.

Let's add a few properties to our animal then.

## Adding properties

Let's start by adding the name of our animal.

We initialize this to None, because when we create an animal we want him to have no name initially.

````python
class Animal:
    name = None  # All animals start with no name
````

We can now access this property and modify this property inside our animal object when we create it.

```python
class Animal:
    name = None  # All animals start with no name


animal_object = Animal()
print(animal_object.name)  # Will be none, because all Animal objects have initial value for name of None
# None
animal_object.name = 'Kuzea'  # We modify the internal value of the name inside animal
print(animal_object.name)  # The new value is inside or new animal object.
# Marius
```

## Adding methods

Methods are added to a class using the same **def** keyword. The only difference between declaring functions and
methods, is that the first argument of a method is **self** (the instance of the object on which the method is called.)

**self** is always present on object methods, and represents the object itself. When calling methods we never pass the
self argument, as python does it for us.

```python
class Animal:
    name = None

    def set_name(self, name):
        """Method that sets the name on an instance of an animal object."""
        self.name = name
```

We can call our newly created method the same way we always call methods.

```python
class Animal:
    name = None

    def set_name(self, name):
        """Method that sets the name on an instance of an animal object."""
        self.name = name


new_animal = Animal()
new_animal.set_name('Kuzea')
print(new_animal.name)  # Printing the modified value of our animals name
# Kuzea
```

We can add more methods to this class to make it more complete.

```python
class Animal:
    name = None
    species = None

    def set_name(self, name):
        """Sets the name of the animal"""
        self.name = name

    def get_name(self):
        """Returns the name of the animal"""
        return self.name

    def set_species(self, species):
        """Sets the name of the species"""
        self.species = species

    def get_species(self):
        """Returns name of the species"""
        return self.species

    def is_species(self, other_species):
        return self.species == other_species
```

Testing our new Animal class

```python
class Animal:
    name = None
    species = None

    def set_name(self, name):
        """Sets the name of the animal"""
        self.name = name

    def get_name(self):
        """Returns the name of the animal"""
        return self.name

    def set_species(self, species):
        """Sets the name of the species"""
        self.species = species

    def get_species(self):
        """Returns name of the species"""
        return self.species

    def is_species(self, other_species):
        return self.species == other_species


animal_1 = Animal()
animal_1.set_name('Kuzea')
animal_1.set_species('Dog')

animal_2 = Animal()
animal_2.set_name('Tuzea')
animal_2.set_species('Dog')

animal_3 = Animal()
animal_3.set_name('Kiskis')
animal_3.set_species('Cat')

print(animal_1.get_name(), animal_1.get_species())
# Kuzea Dog
print(animal_2.get_name(), animal_2.get_species())
# Tuzea Dog
print(animal_3.get_name(), animal_3.get_species())
# Kiskis Cat

print(animal_1.is_species(animal_2.get_species()))
# True
print(animal_2.is_species(animal_3.get_species()))
# False (Dog != Cat)
```

You may now have a questions: If I can directly access the properties of this object, why do I need to use methods ?

### Why use methods

Accessing properties inside an object is always possible in python, but you as a programmer may want to have additional
logic inside your methods to do certain checks or validations.

```python
class Animal:
    name = None
    species = None

    def set_species(self, species):
        if self.species is not None:  # We don't allow to change the species of our animal
            raise Exception('Cannot change the species of an animal after it\'s been assigned')
        if type(species) != str:  # We don't allow to set the species to anything but string
            raise Exception('Species must be a string')
        self.species = species  # We haven't failed above, so we can set our species 

    def get_species(self):
        return self.species

    def set_name(self, name):
        if self.name is not None:
            raise Exception('Cannot set name, as this animal already has a name, please use rename() method')
        self.name = name

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


my_animal = Animal()
my_animal.set_name('Kuzea')
my_animal.set_species(123)  # Will raise error
my_animal.set_species('Dog')
my_animal.set_name('Tuzea')  # Will raise error
my_animal.set_species('Cat')  # Will raise error
my_animal.rename('Tuzea')  # Will work
my_animal.species = 'Cat'
# The last line above will work, but it's not good to do that.
# because we go around the checks that should've prevented us from doing that.
```

## Creating objects with initial value (Constructor functions)

You can also declare classes in a way, that the objects should have an initial value, for this, we need to implement the
constructor function. (Or the initialization method)

For this we need to implement pythons `__init__` method (see below).

```python
class Animal:

    def __init__(self):
        pass
```

The init method is what we use to "initialize" the object. And it has access to our object.

````python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.name = name
        self.species = species
````

Now we can call our constructor functions in a different way, with arguments for name and species

````python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.name = name
        self.species = species


my_animal = Animal('Kuzea', 'Dog')
print(my_animal.species)
# Dog
print(my_animal.name)
# Kuzea
````

We can also have default arguments inside our class declaration, for example

```python
class Animal:
    name = None
    species = None

    def __init__(self, name, species=None):
        self.name = name
        if not species:
            print('Initialized animal without species')
        self.species = species


my_animal = Animal('Kuzea')
```

And we can also do the proper checks if we want to, also inside our class.

The example below creates an animal object

```python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.set_name(name)
        self.set_species(species)

    def validate_name(self, name):
        if self.name is not None:
            raise Exception('Cannot set name, as this animal already has a name, please use rename() method')
        if not name:
            raise Exception('Name should have a value')

    def validate_species(self, species):
        if self.species is not None:  # We don't allow to change the species of our animal
            raise Exception('Cannot change the species of an animal after it\'s been assigned')
        if type(species) != str:  # We don't allow to set the species to anything but string
            raise Exception('Species must be a string')

    def set_species(self, species):
        self.validate_species(species)
        self.species = species  # We haven't failed above, so we can set our species 

    def get_species(self):
        return self.species

    def set_name(self, name):
        self.validate_name(name)
        self.name = name

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


my_animal = Animal(None, None)  # error
my_animal_2 = Animal('Kuzea', 'Dog')
```

## String representations of an object.

If we try to print one of our custom objects, we will notice, that something is not quite right. That is because, all
objects have a "Default" representation of itself in string form, but that may not always be "human-readable".

Example:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


my_animal = Animal('Kuzea', 'Dog')
print(my_animal)
# <__main__.Animal object at 0x0000013EF782AEC8> 
```

The example above shows that the way for python to display this object as a string is with some general information
about the object.

We can change this behaviour by implementing the `__str__` method of our object.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f'Animal with name {self.name} of {self.species} species'


my_animal = Animal('Kuzea', 'Dog')
print(my_animal)
# Animal with name Kuzea of Dog species
```

What we did just now is "overwritten" the string representation of this object. We will learn more about overwrites in
the next lesson.

## A better way to define classes.

Now that we know about init, let's talk about its importance. init is (and should be) the place where we declare all of
our object specific values. This should be done in order to ensure that our class can not be modified from outside.

````python
class ExampleBad:
    value_a = None  # These are values bound to the class, that are also available to the object
    value_b = None


class ExampleGood:

    def __init__(self):
        self.value_a = None  # These are now values that only available to the instance of the object
        self.value_b = None


ExampleBad.value_a = 'Some_value'  # I'm changing the value inside our class directly

ExampleGood.value_a = 'Some_value'  # We assign this value to the class

my_object_bad = ExampleBad()
print(my_object_bad.value_a)
# Some_value
my_object_good = ExampleGood()
print(my_object_good.value_a)
# None

````

In the example above, the first class (ExampleBad) we declared has Class values declarations, and this meant that we
could change the values inside the class, that would affect all new instance of that class.

The second class (ExampleGood), we only declare our instance variables inside the `__init__` method. This means that
when the object is created, we get the values we have inside our `__init__` method. And they can not be changed from
the outside of the class.

### Key lesson

Always declare values that should be accessible only through the instance using the `__init__` method, of have a
separate method that is called inside `__init__` (example below).

```python
class Car:

    def __init__(self):
        self.number_of_windows = 6
        self.number_of_doors = 4
        self.number_of_wheels = 4
        self.engine_power = None


# Or
class Car:

    def __init__(self):
        self._initialize_default_values()

    def _initialize_default_values(self):
        self.number_of_windows = 6
        self.number_of_doors = 4
        self.number_of_wheels = 4
        self.engine_power = None
```

# Using objects to do something useful.

Let's look at an example where our objects actually do useful operations.

We're going to create a class, that will give us an object to easier work with JSON files.

````python
import json


class JsonFileHelper:
    """An object that lest us easily work with JSON formatted files."""

    def __init__(self, file_name: str):
        if not file_name:
            raise Exception('JsonFileHelper requires a filename for the json file.')
        if not file_name.endswith('.json'):
            raise Exception('JsonFileHelper requires the file to be a json file.')
        self.file_name = file_name

    def _get_file(self):
        file = open(self.file_name, 'w+')  # Open file in write mode but also read more (+).
        return file

    def read_json_data(self):
        file = self._get_file()
        json_data = file.read()
        file.close()
        try:
            data = json.loads(json_data)
        except Exception:  # File might not contain anything
            data = None
        return data

    def write_object_to_json_file(self, data):
        file = self._get_file()
        json_data = json.dumps(data)
        file.write(json_data)
        file.close()


# Now we can use this JsonFileHelper to work easily with JSON Files
helper = JsonFileHelper('test_file.json')
data_from_file = helper.read_json_data()
if not data_from_file:  # Checking if we got any data from that file.
    data_from_file = []
data_from_file.append('Some new data')
helper.write_object_to_json_file(data_from_file)
````

# Method and values naming conventions.

As we have seen previously, all properties of an object are easily accessible, at all times, this means that we cannot
"forbid" someone to access a specific property of our object. This is a weakness of python, but developers have come
together and agreed on a specific naming convention that allows us to understand what should and should not be touched.

## Names of classes

Class names should be explicit enough to describe what those classes are meant to represent, but also short.

Besides, class names **can** have any valid variable name. but it doesn't mean it shold

It is a _convention_ that class names should be CamelCase. This means that they should start with an uppercase letter,
and should not contain underscores as separators. Instead, all other words should start with uppercase.

```python
class ObjectWithSpeciesAndName:  # Bad (name is too explicit)
    pass


class Animal:  # Good
    pass


class AnimalList:  # Good
    pass


class animal:  # Bad (but it works)
    pass


class object_with_species_and_name:  # Bad (but it works)
    pass
```

## Method/values names

Method names should follow the same conventions as variable names. But we also have a few special conventions.

Underscores in front of a variable/method names have a meaning.

### Single underscore methods/values

A single underscore means that the developer doesn't want you to access that method or variable from outside the class.

```python
class Example:

    def __init__(self):
        self._secret_value = 'Secret, only for this object'

    def _secret_method(self):
        return self._secret_value  # I can access this value inside the class (as per convention)

    def other_method(self):
        self._secret_method()  # I can use this method because I am working with this class (as per convetion)


my_object = Example()
my_object._secret_value = 0  # I can still change this, but as per convention I know that I am not supposed to to this.
my_object._secret_method()  # I can call this, but I should know that as per convention I should not do this.
```

### Double underscore methods/variables

Double underscore methods and values are usually reserved by python. A good example is `__init__`. This method is
what python expects to initialize the object, `__str__` is also a good example, as python uses this to convert something
to string and/or print objects.

Usually, all double underscore methods/variables are reserved by python. We can still work with them, but we need to
make sure we use them as python intended.

For example, `__str__` should always return a string. Otherwise, we may break some things.