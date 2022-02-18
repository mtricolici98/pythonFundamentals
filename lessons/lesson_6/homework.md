# Homework

Homework for this weekend will challenge all your prior knowledge.

If you find a topic or an exercise that you don't understand I encourage you to "google" for a solution. As long as you
understand the solution, I am happy.

### Also, I want to give each of you a task

## Create a GitHub Account

Those of you who don't have a GitHub account yet, please create one.

I expect the account creation process to not raise any problems for any of you.

## Exercises

**Ex 1**

Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
with those numbers.

_Note: Use str.split() to split the input characters, use str.strip() to remove empty spaces from strings_

```
Input: 
3, 5, 7, 23 

Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
```

**Ex 2**

Write a Python program to print the calendar of a given month and year.

_Note: Use 'calendar' module._

**Ex 3**

Write a Python program to print out a set containing all the colors from color_list_1 which are not present in
color_list_2.

```python
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
```

```
Expected Output :
{'Black', 'White'}
```

**Ex 4**

Write a Python program to convert seconds (from user input) to day, hour, minutes and seconds.

_Note: Don't use any libraries, do the calculations yourself_

Example

```
Input time in seconds: 1234565                                                                                

Output:
14 days 6 hours 56 minutes 5 seconds 
```

**Ex 5**

Create a program that takes temperature as input in Fahrenheit or Celsius. Then convert the temperature to the other
unit.

```python
Celsius = (Fahrenheit - 32) * 5.0 / 9.0

Fahrenheit = 9.0 / 5.0 * Celsius + 32
```

Example:

```
Input: 30 C
Output: 86 F

Input: 50 F 
Output: 10 C
```

**Ex 6**

User inputs **N** in the console.

Write a Python script to print a dictionary where the keys are numbers between 1 and **N** (both included) and the
values are square of keys

Example:

```
Input: 15
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
```

**Ex8.**

Create a python program that will print all combination of numbers a, b, c where a + b + c = **N** where **N** is
input from the console. a, b and c should be greater than 0.

Example

```
Input: 5
Output:
1 1 3
1 2 2
1 3 1
2 1 2
2 2 1
3 1 1
```

**Ex9.**

Create a program that will let the user type any number that is not 0 for as many times as he wants.

After each time the user inputs the number, calculate and show the new sum and average of numbers all numbers that the
user input up until that point.

If the user types 0, the program should stop, and tell the user how many numbers he entered in total.

````
Input: 10
Output:
Sum is 10
Average is 10

Input: 15
Output:
Sum is 25
Average is 12.5

Input: 5
Output:
Sum is 30
Average is 10

Input:0
You've entered a total of 3 numbers
Sum is 30
Average is 10
````
