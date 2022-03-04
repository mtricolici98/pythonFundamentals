# Homework

# Ex 1

Create the classes listed below. Use Inheritance.

For all the properties, use underscores inside the class to hide the properties (example self._inner_color), and declare
get and set methods (example set_inner_color).

Create a Class that describes a **Shape**

The shape class should have the following properties:

* inner color
* border color

Create another class **Circle** which extends **Shape**.

The circle class should have the following additional properties.

* radius

Create another class **Rectangle** which also extends **Shape**

The rectangle class should have the following additional properties.

* width
* length

Create another class **Square** that extends **Rectangle**

The Square class should make sure that the width and length are equal when one of them is set. For example if I set
square.set_length(4), square.get_width() should also be 4.

# Ex 2

Make a new class **NumbersList** that extends the list class.

The **NumbersList** class should only allow for numeric values (int and float) to be added to the list.

This means you have to overwrite the `__init__, append, extend` functions.

Add additional methods as described below:

* get_sum() - returns the sum of all the values
* get_average() - returns the average value of all numbers in the list
