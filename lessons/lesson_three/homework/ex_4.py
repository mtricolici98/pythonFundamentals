temp = int(input('Temperature'))
if temp < 0:
    print('Freezing weather')
elif 0 <= temp < 10:
    print('Very Cold weather')
elif 10 <= temp < 20:
    print('Cold weather')
elif 20 <= temp < 30:
    print('Normal in Temp')
elif 30 <= temp < 40:
    print("It's Hot")
elif temp >= 40:
    print("It's Very Hot")

# Or

if temp < 0:
    print('Freezing weather')
elif temp >= 0 and temp < 10:
    print('Very Cold weather')
elif temp >= 10 and temp < 20:
    print('Cold weather')
elif temp >= 20 and temp < 30:
    print('Normal in Temp')
elif temp >= 30 and temp < 40:
    print("It's Hot")
elif temp >= 40:
    print("It's Very Hot")

# Or

# This will work, so it's not wrong, but it doesn't mean it's right :D See below
if temp < 0:
    print('Freezing weather')
if 0 <= temp < 10:
    print('Very Cold weather')
if 10 <= temp < 20:
    print('Cold weather')
if 20 <= temp < 30:
    print('Normal in Temp')
if 30 <= temp < 40:
    print("It's Hot")
if temp >= 40:
    print("It's Very Hot")

"""
Imagine a version of this code is running somewhere in a thermostat, and the temperature is taken from a sensor. 
The version that uses elif, will only process the comparisons (x < temp < y) until it finds the first one it matches
The version with multiple if-s will process all of them even if it found a match earlier.

If temp wasn't a variable but some value we need to get from the sensor every time,
 this would put a lot of load on the communication between the program and the sensor.
"""
