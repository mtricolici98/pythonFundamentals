## dict

Dict - short for Dictionary is another type of collection. **The biggest difference from a list, is that in a dict, the
values are not accessed by the index but by a 'key'.**

You can think of a dictionary as a collection of pairs each pair consist of a **key** and a **value**.

Dictionary keys can be of any immutable type. Dictionary values can be of any type (including dict)

Dictionaries are good for storing and retrieving data, because dictionaries guarantee that a given value is always going
to be accessible at a given **key**.

Dicts are also very quick at retrieving data when you know the key.

### How to define a dict

Dicts can be defined in two ways.

By calling the constructor

````python
my_dict = dict()  # Empty dict using constructor
my_not_empty_dict = dict(my_key='My value')  # Non-empty dict using constructor
````

By using the curly brackets **{ }**(same as set) but by having the key and value separated by colon  **:**.

````python
my_dict = {'my_key': 'My value'}
````

### Why use dicts

Dicts offer nice ways to store dynamic data

For example, we may want to store a person information:

```python
me = {
    'name': "My name",
    'age': 20,
    'profession': 'Policeman',
    'hobbies': ['Music', 'Reading sport books', 'Finding purpose in life']
}
```

This allows us to then store multiple pieces of such information, in a list or a file.

I personally like to thing of them as dynamic objects, because a dict can be used to represent whatever you like, and
can be modified at runtime.

### Working with dicts

Dicts behave like a combination of **set** and **list**.

Values in sets can be iterated over, have length, and can be accessed using the square brackets like a list, but because
the keys have to be unique, dict keys can be looked at as sets of keys.

```python
my_dict = {1: 'A', 'two': 'TWO', 'a': 3}
len(my_dict)  # 3
```

#### What can be inside a dict ?

Dict **values** can be of any type, including dict.

Dict **keys** should be an immutable data type

#### Accessing values

Accessing values is possible by asking for the value at a key.

If the key is not present, an error will be raised.

````python
my_dict = {'my_key': 'My value'}
print(my_dict['my_key'])  # My value
````

#### Adding/Changing values

Adding or changing values in a dict is done by assigning a value to a new key to add a new pair, or by assigning a value
to an existing key to update its value.

An error will not be raised if a key does not exist during assignment, only during "access".

````python
my_dict = {'my_key': 'My value'}
my_dict['my other key'] = 'My other value'
print(my_dict['my other key'])  # My other value
````

Values in a dict can be passed direclty or as a refernce.

## Object references

In Python, assigning to a variable the value of another **mutable** variable, will result in creating another reference
to the same value.

```python
some_list = [1, 2, 3]
also_some_list = some_list
```

In the example above, we now have 2 variables that both point to the same list. Updating the list using either of those
values will updated the list itself, not just the "reference".

```python
some_list = [1, 2, 3]
also_some_list = some_list
also_some_list.append(4)
print(some_list)  # [1, 2, 3, 4]
```

You must handle your references with care, as it may result in data being modified without your consent.

### Cloning

Immutable data types are cloned by default when they are assigned to a new variable

If you want to make a clone of a mutable data type (ex: **some_list**) you can do so using the list constructor or using
the .copy method of the list.

```python
some_list = [1, 2, 3]
some_list_clone = list(some_list)
also_clone = some_list.copy()
some_list_clone.append(4)
print(some_list)  # [1, 2, 3]
print(some_list_clone)  # [1, 2, 3, 4]
print(also_clone)  # [1, 2, 3]
```

## Iteration

Iteration through a dict is possible, and will return the keys of the dict.

````python
my_dict = {'first': 1, 'second': '2', 'third': [1, 2, 3]}
for key in my_dict:
    print(my_dict[key])
# 1
# 2
# [1, 2, 3]
````

#### Values Or Keys only

It's possible to iterate only through the keys or the values of a dict.

```python
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for a in my_dict.keys():
    print(a)
# 1
# 2
# 3
for a in my_dict.values():
    print(a)
# one
# two
# three
```

### Dicts can be nested

Yes, you can have a dict inside a dict, as many as you want in fact. This is useful for when you want to create very
flexible 'data structures', but don't want to have something permanent.

```python
flights = {
    'Air Moldova': {
        'Incoming': [dict(number='AA1110', source='Frankfurt, DE', destination='Chisinau, MD')],
        'OutGoing': [dict(number='OB1110', source='Chisinau, MD', destination='Milan, IT')],
    }
}   
```

Making these dicts manually can be a hassle, but working with them programmatically is much more convenient and
flexible.

For example, I could print a list of all incoming flights from Air Moldova

```python
for flight in flights['Air Moldova']['OutGoing']:
    print(flight['number'], flight['source'], flight['destination'])
```

#### Items

It is also possible to get access to both the key and the values at the same time using the **.items()** function.

```python
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key, value in my_dict.items():
    print(f'Key {key}, value {value}')
# Key 1, value one
# Key 2, value two
# Key 3, value three
```

## Unpacking

**Unpacking** in python is the process of extracting (unpacking) individual values from a collection.

For now let's try out unpacking on tuples

Tuples are perfect for using together with unpacking because they are fixed size, so you can always know what to expect
from a given tuple, but lists work too, but I encourage you to try it yourself.

```python
my_tuple = (10, 20)
# MyTuple gets unpacked into a and b (a takes the first element from the tuple and b takes the second one)
a, b = my_tuple
print(a)  # 10
print(b)  # 20
```

Here's an example of unpacking more than 2 values

```python
some_tuple = (10, 30, 'Yes')
width, height, condition = some_tuple
```

And here's an invalid example.

You can't unpack less or more values than expected.

```python
tup = (10, 12)
a, b, c = tup  # Raises Error
```

Unpacking can be done with any size of a collection, but there's a point at which we reach diminishing returns, so use
it mindfully.

## The IN keyword checking if something is inside a collection

Let's say we have a collection of elements.

We want to check if a specific element in inside that list.

Let's say we have a bunch of names, these are the names of people we have at our school.

Now let's say I want to know if one specific name is inside that list.

One way to do it will be like this

```python
name_list = ['Ana', 'Andrei', 'Dana', 'Dima', 'Cristina', 'Petru', 'Ion', 'Vaniusha']
name_to_find = input()
for name in name_list:
    if name == name_to_find:
        print('Found')
```

Python provides an easier way to achieve this: The **in** operator.

```python
name_list = ['Ana', 'Andrei', 'Dana', 'Dima', 'Cristina', 'Petru', 'Ion', 'Vaniusha']
name_to_find = input()
if name_to_find in name_list:
    print('Found')
```

The **in** operator is also called the operator of "belonging", it checks if a value "belongs" in a collection.

For dicts, **in** checks only the keys by default.

````python
my_dict = dict(a=1, b=2, c=3)
print('d' in my_dict)  # False
print('c' in my_dict)  # True
print(3 in my_dict)  # False
print(3 in my_dict.values())  # True
````

# Homework

**Ex1.**

1. Ask the user to input a large text with many words. Ignoring punctuation.
2. Calculate how many times each word (regardless the case) was used.

Solve this exercise once using **dicts** and another time using **sets**

Hints:
Use `str.split(' ')` to break down the text into a list

````
Example:
Input:
how much wood would a woodchuck chuck if a woodchuck could chuck wood
Output: 
Word "how" was used 1 times.
Word "much" was used 1 times.
Word "wood" was used 2 times.
Word "would" was used 1 times.
Word "a" was used 2 times.
Word "woodchuck" was used 2 times.
Word "chuck" was used 2 times.
Word "if" was used 1 times.
Word "could" was used 1 times.
````

**Ex2.**

Create a program that will register **n** people in a system. (n is a number input by the user)

For each person register their:

* First name
* Last name
* Age
* Profession

**If the age of the person is below 14 do not register.**

After registering each person. Print out the following:

Registration for the {profession_name} {first name} {last name} aged {age} is complete.

After registering all **n** people. Create 4 lists of people.

1. People between ages 14 and 18 (including)
2. People between ages 18 (excluding) and 25 (including)
3. People between ages 26 and 45 (including)
4. People above age 45

Print out the names of each in the given format:

```
Users between 14 and 18 are: name1, name2 ...

Users between 18 and 25 are: name1, name2 ...

Users between 26 and 45 are: name1, name2 ...

Users above 45 are: name1, name2 ...
```

**Ex3.**

Create a program that will register a list of guests and food for a restaurant.

The user has to input how many guests will be coming

To register each guest, the user will input the **name** of the guest and two (2) **dishes**.

At the end, print out the list of the guests and what they ordered. And the total number of each dish the restaurant
will have to prepare.

```Example
Input:
3

Marius
Ravioli
Caesar Salad

Ana
Pepper steak
Caesar Salad

Gheorghe
Greek salad
Lentil Soup

Output:
The guests will be: [Marius, Ana, Gheorghe]

Marius ordered Ravioli and Caesar Salad 
Ana ordered Pepper steak and Caesar Salad 
Gheorghe ordered Greek salad and Lentil Soup
 
You will have to prepare:
Ravioli x 1
Caesar Salad x 2
Pepper steak x 1
Greek salad x 1
Lentil Soup x 1
```


