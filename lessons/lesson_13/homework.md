## Homework

# Ex1

Write a Python program to square and cube every number in a given list of integers using Lambda

Original list of integers:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
Square every number of the said list:
`[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
Cube every number of the said list:
`[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`

# Ex2

Write a Python program to find palindromes in a given list of strings using Lambda. Orginal list of strings:
`['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']`
List of palindromes:
`['php', 'aaa']`

# Ex3

Create a decorator that checks if the result of the function it decorates is always a number

The decorator should be called "validate_numeric" and should raise ValueError when the result of function it decorates
is not numeric.

# Ex4

Create a generator function, that generates a new user input every time.

The generator function should take stop_at as an argument, if the input string is the same as stop_at. The generator
should stop yielding results.

Example usage:

```python
for user_input in my_user_input_generator('STOP'):
    print(user_input)
```