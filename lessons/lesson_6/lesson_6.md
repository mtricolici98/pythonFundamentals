# Lesson 6

### Useful links

[Datetime Format](https://www.programiz.com/python-programming/datetime/strptime)

[Math Library](https://docs.python.org/3/library/math.html)

[List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

## List comprehension

One of my (and probably everyone's favourite feature in Python) is list comprehension.

List comprehension allows developer to perform actions on a list of items with a compact and beautiful syntax.

Let me show you.

```python
some_numbers = [1, 2, 3, 4, 5]
numbers_doubled = [number * 2 for number in some_numbers]
print(numbers_doubled)  # [2, 4, 6, 8, 10]
```

Which is the same as

```python
some_numbers = [1, 2, 3, 4, 5]
numbers_doubled = []
for number in some_numbers:
    numbers_doubled.append(number * 2)
print(numbers_doubled)  # [2, 4, 6, 8, 10]
```

You can nest comprehensions

```python
number_box_1 = [1, 2, 3]
number_box_2 = [4, 5, 6]
numbers_combined = [n_1 * n_2 for n_1 in number_box_1 for n_2 in number_box_2]
print(numbers_combined)  # [4, 5, 6, 8, 10, 12, 12, 15, 18]
```

Some useful scenarios.

Extracting list of data from a dict

Say you have a list of people. And you want to extract only their names.

````python
students = [
    dict(name='Andrei', age=22, gender='M'),
    dict(name='Cristina', age=35, gender='F'),
    dict(name='Victor', age=18, gender='M'),
]

student_names = [student['name'] for student in students]
````

### Conditional list comprehension

You can apply conditional expressions inside list comprehensions.

In order to do so, use the **if** statement like shown below.

```python
numbers = [1, 2, 5, 20, 28, 37, 54, 29, 300]
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)  # Prints [1, 5, 37, 29]
```

Compared to traditional if statements, the **if** condition in list comprehensions doesn't have an **else** or **elif**

## Break

**break** is a keyword in python, that allows us to **break** the loop.

It will stop any loop from continuing its execution.

```python

for a in range(1, 1000):
    if a == 50:
        break
    print(a)
# Will print numbers up to 50
```

**break** is very useful to us as it allows us to get rid of unnecessary iterations.

For example, we have a task, to see if total score of all members of a class is higher than 100

```python
members = [{'name': 'SomeName', 'score': 30}, ...]
````

We could use sum to figure out the total score of all the members and then compare it to 100

```python
total_score = sum([member['score'] for member in members)
print(total_score > 100)
```

But we only care to check if score is higher than 100, and we don't need the total score. If there are thousands or many
thousands of members, we will be doing unnecessary iterations, that may affect performance.

```python
members = [{'name': 'SomeName', 'score': 30}, ...]
score = 0
score_higher_than_100 = False
for member in members:
    score += member['score']
    if score > 100:
        break
```

## While Loops

While loops are the most basic type of loop in programming. They follow the simple principle of "while condition is
true, repeat the block."

While loops in python can be declared using the **while** keyword, followed by the condition

```python
while True:
    print("I will run forever")
```

The example above will print "I will run forever" forever, because the condition is set to True and can never change.

This example above is an example of what not to do in programming.

A better example would look like this.

````python
should_keep_runnning = True
while should_keep_runnning:
    print('I\'m still running')
    stop = input('Should I stop ? (Type stop)')
    if stop.lower() == 'stop':
        should_keep_runnning = False
````

In this second example, we alter the value of the condition under which the loop repeats, and by doing this, we stop the
loop.

### Breaks

As with for loops, breaks allows us to stop any while loop, even a **while true:** one.

This allows us to re-write the previous example using breaks

```python

while True:
    print('I\'m still running')
    stop = input('Should I stop ? (Type stop)')
    if stop.lower() == 'stop':
        break
```

The loop in the example above will stop only when the **break** is applied.

### When use while loops

**For** loops are used to iterate a collection, or do something a finite (or known) ammount of times

**While** loops are best used when you don't know how many times something should run.

For example, we may let the user, add words to a list of words, for as much as he wants, until he types **stop**.

````python
word_list = []
while True:
    word = input("Type a word to add it to the list or stop to print the list")
    if word == 'stop':
        break
    word_list.append(word)
print(word_list)
````

You can use for loops to iterate through a collection as well

```python
my_list = list(range(10))
index = 0
while index < len(my_list):
    print(f'Element {index} from the list is {my_list[index]}')
    index += 1
```

## Bult-in modules

### math

The math built-in library offers a variety of useful functions to work with numbers

Mathematical and Arithmetical operations are available, alongside some other functions

Check out their description [here](https://docs.python.org/3/library/math.html)

```python
import math

print(math.sqrt(9))  # Calculates square root
print(math.cos(10.5))  # Calculates cos
print(math.sin(10.5))  # Calculates sin
print(math.factorial(5))  # Calculates factoeal
print(math.ceil(5.3))  # Rounds up
print(math.floor(5.3))  # Rounds down
```

### time

time is a builtin library that allows us to work with, well you guessed it, time

Commonly used functions are

time.time() - It returns the number of seconds passed since epoch. For most systems (Unix based) the epoch started at
January 1, 1970, 00:00:00 so time.time() will return the number of seconds since then

````python
import time

print(time.time())
# 1645170265.7333522
````

Useful scenarios of usage is when you want to check the nr of seconds a program or a piece of program ran for.

```python
import time
import math

# Factoreal calculation
number = int(input('Number to calc factoreal'))
started_at = time.time()
acc = 1
for a in range(1, number + 1):
    acc *= a
stop_at = time.time()  # Returns current time in seconds every time
print(f'My solution ran for {stop_at - started_at}, result is: {acc}')

started_at = time.time()
result = math.factorial(number)
stop_at = time.time()
print(f'Python solution ran for {stop_at - started_at}, result is: {result}')
```

After running the above example we'll see a result similar to this

```
Number to calc factoreal 120
My solution ran for 0.0, result is: 6689502913449127057588118054090372586752746333138029810295671352301633557244962989366874165271984981308157637893214090552534408589408121859898481114389650005964960521256960000000000000000000000000000
Python solution ran for 0.0, result is: 6689502913449127057588118054090372586752746333138029810295671352301633557244962989366874165271984981308157637893214090552534408589408121859898481114389650005964960521256960000000000000000000000000000
```

Both examples ran very fast. This is probably because the interpreter caught onto the fact that we want to calculate a
factorial value, and optimized the run time.

#### Using time to pause execution

time has another commonly used function called .sleep() - Sleep will pause the execution of the program for n number of
seconds.

Example:

```python
import time

for a in range(10):
    print(f'Iteration nr {a + 1}')  # This print statement will be executed every 1 seconds for 10 times
    time.sleep(1)
```

## datetime

If time is a library that allows us to work with system time. Datetime is a library that helps us work with human time.

```python
from datetime import datetime

print(datetime.now())
```

datetime contains multiple useful objects

Most used are the following. **datetime**, **date**, **time** and **timedelta**.

datetime is used to represent both date and time at the same time

date can represent only dates

time can represent only time

timedelta is used to represent datetime differences (ex. 1 days 2 hours)

````python
from datetime import datetime, timedelta

date_today = datetime(2022, 2, 18, 18, 30)  # Declaring a datetime object
date_yesterday = datetime(2022, 2, 17)  # Declaring a datetime object without time
print(date_today - date_yesterday)  # 1 day, 18:30:00 - Result is a timedelta

in_one_day = timedelta(days=1)  # Declaring a custom timedelta
one_day_from_now = datetime.now() + in_one_day  # Operations with timedelta
if one_day_from_now > datetime.now():
    print(f'{one_day_from_now} is in the future')
````

Working with only time or dates:

```python
from datetime import time, date

human_time = time(12, 30)
print(human_time)  # 12:30:00
human_date = date(2022, 12, 31)
print(human_date)  # 2022-12-31
```

It is also possible to format strings into dates and vice-versa. See full
explanation [here](https://www.programiz.com/python-programming/datetime/strptime)

```python
from datetime import datetime

string_date = '2022-12-31'
# Formatting string to date-time object
datetime_date = datetime.strptime(string_date, '%Y-%m-%d')
print(datetime_date)  # 2022-12-31 00:00:00
# More examples, different formatting
print(datetime.strptime('28/02/2022', '%d/%m/%Y'))
print(datetime.strptime('2022/28/02', '%Y/%d/%m'))

# Formatting datetime object to string (for custom formatting)
print(datetime.now().strftime('%Y-%m-%d'))
# 2022-02-18
print(datetime.now().strftime('%a %d %B %Y'))
# Fri 18 February 2022
```

### Other built-in modules

Python has a lot of built-in modules. Check them out yourself. Try some out if you find any of them
interesting. [Python builtin list](https://docs.python.org/3/py-modindex.html)

## Performance

Let's stop a bit, and discuss computation efficiency.

Every code instruction has a cost, some operations are very "expensive" and others are "cheap". But when developing
software, it is very important to understand why something can be slow.

### Time complexity (Big-O)

The Big **O** is a common metric in programming that defines time complexity, that is, the time to execute a task in
relation to the input size.

Let's consider a short example.

```python
for a in some_list:
    print("a")
```

Lets assume that in the example above, the Print instruction takes 1ms. This means that the time of execution of the
above instruction depends on the length of the list, which is Unknown.

From this, we can make a educated guess, that the time to execute will grow linearly with the size of the list, and will
result in a time complexity of **O(n)**, where **n** is the size of the input.

Big-O always assumes the worst case scenario.

If we look at this example below, the execution may stop at the first iteration, or it may go on for many cycles until
it finds a **1** in the random list of numbers. This is why the time complexity is O(n), since we can't control the
input.

```python
b = input()
for a in random_list:  # from 1 to infinity
    if a == b:
        print('Something')
        break
```

Common Complexity Examples:

**O(1)** - Constant time - Times remains constant regardless of the input size

```python
print(random_list[1])  # Constant time
print(some_dict['my_key'])  # Constant time
print(my_key in some_dict)  # Constant time
```

**O(n)** - Shown Previously - Also called linear time - time grows linearly with the input size (n)

More examples of **O(n)**

```python
random_list = [...]
print(10 in random_list)  # Could check all elements in random_list
```

**O(n2)** - Shown below - Also called quadratic - time is proportional to the square of the input size - Often found in
nested loops

```python
for a in range(n):
    for b in range(n):
        print(a * b)
```

If you're interested to see more about time complexity, please
read [here](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)
