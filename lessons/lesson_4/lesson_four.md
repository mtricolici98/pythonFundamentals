# Lesson 4 - Collections

## What we've learned

1. Base Data types
2. if statmeents
3. String formatting

## What are collections.

Up until now we worked mostly with basic data types, integer, floats, strings. These data types hold one value very
well, but it's often the case that we want to store more than one thing in a variable. Collections are data types that
allow us to store more than one value.

## Lists

List is probably the most commonly used collection. It is just what it says, a list of items.

Items can be of any type, for example you can have 3 numbers and 2 words in the same list. This is not always the case
in **other** languages.

List items are:

* Ordered - They maintain the order in which they have been added
* Changeable - You can change any item in the list regardless of its order
* Non-Unique - You can have more of the same value anywhere in the list

There are two ways we can declare an empty list.

Using the list **constructor** or using the square brackets (**[ ]**).

```python
my_list = list()
also_list = []
```

It's also possible to create non-empty lists.

```python
non_empty = [1, 2, 3]
```

### A collection you already know.

As we've worked with strings, I've mentioned that it's mostly a list of characters and behaves like one.

### Accessing values

List values can be accessed using the index of their position in the list. As with strings, the index starts at 0.

```python
my_list = ['first', 'second', 'third']
print(my_list[0])  # first
print(my_list[1])  # second
print(my_list[2])  # third
print(my_list[3])  # Error
```

You can of course using negative indexes or get a sub-list of items from a list.

```python
my_list = ['one', 'two', 'three']
print(my_list[-2])  # two
print(my_list[-2:])  # ['two', 'three']
print(my_list[0:2])  # ['one', 'two']
```

### Lists are mutable

This means that values inside a list can be changed freely or added freely without creating a new instance.

Changing elements in a list is done by assigning a new value to the element at a specific index.

```python
my_list = [1, 2, 3]
my_list[1] = 4
print(my_list)  # [1,4,3]
my_list[1] = 'two'
print(my_list)  # [1,'two',3]
```

### Adding elements to a list

Adding elements to a list can be done in two main ways.

1. By using the **.append()** function
2. By combining with another list (list concatenation)

```python
my_list = []
# Using the append
my_list.append('First item')

# Concatenating lists (same as string concatenation) will add the two lists together
my_list = my_list + ['Second Item']

# OR

my_list += ['Second Item']

print(my_list)  # ['First item', 'Second Item']
```

List concatenation is also possible using a dedicated function **.extend()**

### Removing items from a list

#### Using remove()

It is also possible to remove an item from a list using the **.remove()** function. It is

```python
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)  # [2,3]
```

The **.remove()** function, removes the first occurrence of the item, if there are multiple items with the same value,
only the first one will be removed.

```python
my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)  # [1,2,3]
```

If no items are found in the list with the same value as the one you want to remove, it will result in an error.

#### Using .pop()

Remove will delete the item from the list, but sometimes you want to access the value before removing it. This is
where **.pop()** comes in.

.pop() uses the index of the item to remove it from the list and return it to the user.

```python
my_list = ['First', 'Second']
a = my_list.pop(0)  # Removes first element of the list and assigns it to 'a'
print(a)  # 'First'
print(my_list)  # ['Second']
```

If no arguments are passed to **.pop()** it will remove the last item in the list.

```python
my_list = ['First', 'Second']
a = my_list.pop()  # Removes last element of the list and assigns it to 'a'
print(a)  # 'Second'
print(my_list)  # ['First']
```

### More list functions

```python
my_list = [1, 3, 5, 7]
my_list.reverse()
print(my_list)  # [7,5,3,1]
list_length = len(my_list)  # Calculates the length of the list 
print(list_length)  # 4
new_list = [22, 34, 12, 42, 24, 22, 34]
count_of_22 = new_list.count(22)  # Counts number of occurrences 
print(count_of_22)  # 2
sorted_list = sorted(new_list)  # Sorts the list
print(sorted_list)  # [12, 22, 22, 24, 34, 34, 42]
```

Feel free to experiment with other possibilities of the list.

## Tuples

Tuple is a very basic collection. And is the closest thing we have in Python to an Array. It is immutable, so it can be
only used to store or move data. Tuples are great for storing temporary data or large amount of unchanging data. Tuples
are far more memory efficient than lists, because as a collection, it is fixed in size, which means that the interpreter
knows exactly how much computer memory to allocate for it.

A tuple is declared using the parenthesis **( )**, with items separated by a comma **,** .

```python
my_tuple = (1, 2, 3)
```

You can access data from a tuple, but you cannot add or change the data, same as a String

You can combine (concatenate tuples) as you can concatenate strings.

```python
my_tuple = (1, 2, 'three')
print(my_tuple[2])  # 'three'
my_tuple[2] = 3  # Error - Assigning values is not allowed
bigger_tuple = my_tuple + (4, '5', 'six')
print(bigger_tuple)  # (1, 2, 'three', 4, '5', 'six')
```

Tuples don't have the .append/.add/.remove methods available.

### Why use tuples ?

Tuples should be used in two scenarios:

1. When you have data that should not be changed
2. When you have a lot of data that you know will not change, because tuples require less computer memory.

## For loops, iteration

Another one of the main pillars of programming, iteration.

**Iteration** is the process of doing same thing multiple times with different values

In the example below, we can go through the values inside the list, and perform operations on it.

This basic example, only prints out the value of each element

**For** loops are done using the **for ... in ...** blocks in python.

```python
my_list = ['First', 'Second', 'Third']
for element in my_list:
    print(element)
# First
# Second
# Third
```

You can iterate through tuples same as with any other collection

````python
data = (52, 29, 39)
for el in data:
    print(el)
````

Let's consider a more practical example. Let's calculate the sum of a list of numbers.

```python
my_numbers = [10, 20, 14, 92, 20]
numbers_sum = 0  # Initialization of our collector variable
for number in my_numbers:
    numbers_sum = numbers_sum + number  # Adding to our collector variable
print(numbers_sum)
```

The basic example above shows you the ability to go through a list of values. And perform operation with the values form
the collection.

## Range

Sometimes, you want to iterate a certain number of times, but don't have a list to go by.

For example, you might want to do something 5 times. This is where the **range()** function comes in.

**range()** will create a "list" based on parameters supplied to it.

````python
for a in range(5):
    print(a)
# 0
# 1
# 2
# 3
# 4
````

The example above will print 0, 1, 2, 3, 4

The **range** function supplies us with values, one after another.

It's possible to customize multiple things about range function.

For example, we might want to start at 1 instead of 0. We should also adjust the end number.

```python
# Start at 1, end at 6 (exclusive) 
for a in range(1, 6):
    print(a)
# 1
# 2
# 3
# 4
# 5
```

If only one argument (**end**)  is provided to **range** it will start at 0 and iterate until it reaches the number
supplied in the argument.

If two arguments are provided (**start** and **end**), it will start from the number in the first argument, and go on
until the number in the second argument.

It is also possible to provide the **step** argument to the range function. It will indicate how much should the number
increase in between iterations. Default is 1, but we can customize it. See example below:

```python
# Start at 0, end at 10 (excluding 10), step is 2
for a in range(0, 10, 2):
    print(a)
# 0
# 2
# 4
# 6
# 8
```

### Negative ranges

It is possible to iterate downward into negative numbers, if you supply a negative step value.

````python
for a in range(0, -5, -1):
    print(a)
# 0
# -1
# -2
# -3
# -4
````

### Iterating a list using range

```python
my_list = [6, 9, 4, 2, 0]
for a in range(len(my_list)):  # len(my_list) == 5
    print(f'Item at index {a} is {my_list[a]}')
# Item at index 0 is 6
# Item at index 1 is 9
# Item at index 2 is 4
# Item at index 3 is 2
# Item at index 4 is 0
```

Using the range function, we get supplied numbers that can be used as indexes.

In the example above, we use the range that is as long as our list, so each iteration in the range will match the index
of the position in the collection.

This can be further improved to work on two lists simultaniously for example:

```python
list_1 = ['a', 'b', 'c']
list_2 = [97, 98, 99]
for index in range(len(list_1)):
    print(f'Letter {list_1[index]} has position {list_2[index]} in ASCII.')
```

The example above can perform operations on both lists, as it works using indexes instead of working with collections
directly.

### When is range helpful ?

1. When we want to do something a finite number of times
2. When we want to know the index of an item
3. When we want to know the count of the iterations.

### What can we do inside an iteration (for loop)

Anything

Examples:

1. Asking user input

```python
my_list = [2, 3, 4]
for a in my_list:
    print(f'Processing {a}')
    b = int(input('B'))
    print(f'{a} * {b} = {a * b}')
```

This is better done with [range](#range)

2. Another Iteration

Ex: Calculating numbers from one list multiplied with numbers from another list.

```python
first_list = [10, 20, 30]
second_list = [90, 80, 70]
for a in first_list:
    for b in second_list:
        print(f'{a} * {b} = {a * b}')
```

3. Populate some other list

```python
number_list = [2, 3, 4, 5]
power_two_list = []
for number in number_list:
    power_two_list.append(number ** 2)  # a to the power of 2
print(power_two_list)  # [4, 9, 16, 25]
```

4. Conditional processing

```python
number_list = [23, 39, 48, 100]
numbers_under_50 = []
numbers_above_50 = []
for number in number_list:
    if number < 30:
        numbers_under_50.append(number)
    else:
        numbers_above_50.append(number)
```

## set

Set is similar to a list, with the main difference being that a set holds only unique values.

Sets are initialized using the **set()** constructor or by placing the items inside the curly brackets **{ }**.

```python
my_set = set()  # Constructor initialization
also_set = {}  # direct initialization
```

You can also pass a list (or other collection) to the set constructor, to generate a set out of the provided collection.
Or just initialize a set with initial values.

```python
my_list = [1, 2, 3, 3, 4, 5, 5, 6]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4, 5, 6}
print({1, 2, 2, 3})  # {1, 2, 3}
```

We add elements to a set using the **.add()** function

```python
my_set = {1}
my_set.add(1)  # Does nothing
my_set.add(2)  # Adds two
```

We can also add a collection of elements (similar to the list **.extend** or list concatenation)

```python
my_set = {1, 4, 6}
my_set.update([2, 4, 10])
print(my_set)  # {1, 2, 4 ,6, 10}
```

### You can't access a specific value in a set

```python
my_set = {1, 2, 3}
my_set[0]  # Error
```

Accessing items in a set using indexes is forbidden.

### Why use sets ?

Sets are useful when you want to work with unique data, aggregate into unique data.

For example: You want to check what users posted the last 1000 comments on a video. Some users might've posted 2 or more
comments, so if you aggregate them in a set, you will be left with values for unique users that commented within the
last 1000 comments in a video.

````python
users = set()
for comment in comments[-1000:]:
    users.add(comment.user)
````

## Homework

**Ex1**. Having a list Ex: [32, 19, 39, 30]

Write a program that will calculate and:

1. Print the length of the list
2. Print the sum of the numbers in the list
3. Print the numbers from the list that are even

```
Example:
my_list = [32, 19, 39, 30]

Output:
Length is 4
Sum is 120
Even numbers are [32 , 30]
```

**Ex2.**

1. Ask the user to input a number **n**. Following that, for **n** times:
    1. Ask the user to input a number and add the number to the list.
2. After the user has input all the numbers, calculate the average value of the numbers in the list and print it

````
Example:
Input:
3
48
24
36
Output: 
Average is 36.0
````

**Ex3.**

We are going to create a program where we find find the person with the highest score.

1. Ask the user to input a number **n**. Following that, for **n** times:
    1. Ask the user to input a name (name of the person), and add it to a list
    2. Ask the user to input a number (the score of the person) and add it to another list
2. After the user has input all values, find the highest score in the list, and print the name of the person with the
   highest score.

````
Example:
Input:
3
Ana
80
Mircea
94
Cristi
89
Output: 
Mircea are cel mai mare scor
````

**Ex4.**

Create a program that is going to take a whole number as an input, and will calculate the factorial of the number.

Factorial example: 5! = 5 * 4 * 3 * 2 * 1 = 120

````
Example:
Input:
5
Output: 
120
````
