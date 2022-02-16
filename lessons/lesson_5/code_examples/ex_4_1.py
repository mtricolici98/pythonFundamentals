# How many times was a value was input from console after N inputs solution using sets

values_list = []

times = int(input('How many numbers ? '))

for i in range(times):
    name = input('Input a value')
    values_list.append(name)

# Creating a set from our list of values
for name in set(values_list):
    print(f'{name} was input {values_list.count(name)} times')

# Yes I know this is shorter :) the only way dict has as a benefit is the performance.

"""
In the dict example we do 2 loops

One where we get the data from input
Another one where we print the results

---------------------------------------------------
In this example we do 4 loops

One where we get the data from input
Second one where we convert values_list to set
    Yes, converting a collection to another will iterate in the background through all of the elements 
Third one when we iterate through set of values_list
Fourth one is when we count the occurrences using .count() !! AND THIS ONE IS DONE FOR EVERY SINGLE VALUE 
--------------------------------------------------------

This small difference is nothing special in our case with ~ 10 values, but when you have to quickly do it for 10k, it's starting to show.

For 10k times (without the input) it takes 0.6seconds with dict and 0.9 seconds with set

For 100k iterations (also without input) it takes 0.6 seconds using dict, and 97 seconds using set :) 

Message me if you want to see the code of the testing.
"""
