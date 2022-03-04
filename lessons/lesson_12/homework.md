# Homework

# Ex 1.1

Using your classes **Shape**, **Circle**, **Rectangle** and **Square**.

Implement the necessary methods to:

* Get the area of the shape (Circle, Rectangle, Square), as a property. Except for Shape (shape can't have an area)
* Be able to compare shapes (only shapes of the same type can be compared)
    * Only shapes of the same type can be compared:
        * I should be able to compare a Circle with another circle
        * I should not be able to compare a Circle with a Square
    * I should be able to compare a Square and a Rectangle, because they have the same properties.
    * When comparing Rectangles, compare the area of the rectangle (not the width and length)
* Be able to perform addition, subtraction and multiplication of shapes (for example _rectangle1 + rectangle2_)
    * When performing such operations, perform the operations on the common properties of the 2 objects (
      width/length/radius)
    * When performing subtraction, the value of properties of a shape should not be less than 0.
    * Only shapes with the same properties can have the operations performed (ex: Circle and Square can not be added,
      Square and Rectangles can). You can use the isinstance and issubclass checks to perform the checks.
    * When performing multiplication, also allow to multiply the object with a number.
        * Example: Rectangle(2,4) * 2 = Rectangle(4,8)

# Ex 1.2

Create a Shape service.

The methods inside shape service should all be staticmethods.

The Shape service should have the following properties as class properties:

DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - You can choose any string default values

The Shape service should have the following methods:

* create_default_circle(radius) - creates and returns a Circle object, with properties for colors form the defaults.
* create_default_rectangle(width, length) - creates and returns a Rectangle object, with properties for colors form the
  defaults.
* create_default_square(side_length) - creates and returns a Square object, with properties for colors from defaults.
* color_shapes(list_of_shapes, inner_color, border_color) - set's the colors of all the shapes in the list to the colors
  from the arguments.

# Ex 2.

If you take a look at the file [conversion_rates.json](conversion_rates.json) You will see a very long list of all
currencies and their conversion rate from and to MDL.

## Task

Create a program that is going to load this list into the program.

On program start-up, show the list of all possible conversions, with rates from lowest to highest.

Let the user input the name of the currency to convert to. Example: EUR or MDL

* If the input currency is MDL, then use the ask the user to input again what currency to convert to MDL. Example USD
    * Let the user input the value of MDL to convert to that currency.
    * Print the converted value with only 2 decimal points (example 92.43)
* If the input currency is not MDL, then:
    * Let the user input the value of MDL to convert to that currency.

## Conditions

* The entire program should be object-oriented (only use classes), except for the main.py which will run the program
* You should create CurrencyConversion object, that will store all information about each conversion.
    * Example. CurrencyConversion(from="MDL", to="EUR", rate=0.049175765442905, inverse_rate=20.335219818002, name="
      EUR")
* In order to have the ability to sort CurrencyConversion objects, implement `__gt__, __lt__, __eq__, __le__, __ge__`
  functions. These functions should compare the rates of the CurrencyConversion objects.
* Have a CurrencyConversionService that will manage all the currency conversion information, and should have at least
  this method below.
    * convert(from_currency, to_currency, amount)

## Considerations

The json contains a dict of dicts. It's not a list, so pay attention, and analyze the data you are working with before
you start.

# Optional: Assignment 1

This Assignment is a big one, and will require a lot of your time. You can start whenever you feel ready, and finish it
whenever you will.

I am confident that all of you are able to solve this exercise, but it will take a lot of time. Don't get frustrated if
you can't do it in one day. (It took me more than one day to solve this too)

For this project, create a separate GitHub project. You can send me the project when you think you have finished.

All the data for this program (users, reservations, rooms) should be stored in files.

# Task

Create a software console application which main purpose should be handling reservations in the hotel.

The application should be multi-user. When the application is started up, the user should login.

# Requirements

### Roles Within a system a few roles would operate:

* Guest
    * Can book a hotel's room/rooms
    * Can cancel a reservation
    * Can see a list of free rooms and their prices
* Front desk
    * Is responsible for the actual booking of a room.
    * Can cancel a reservation
    * Can see a list of free rooms
    * Can see a list of reservations
* Administrator:
    * Can see a list of rooms and their prices
    * Can create a new room
    * Can change a price of a room

### In the hotel there are 3 types of rooms:

* Single room
* Double room
* Apartment (contains 1 double bed and 2 single beds)

### The hotel rooms have the following prices:

|          | Single | Double | Apartment |
|:--------:|:------:|:------:|:---------:|
| Ordinary |   50   |   80   |     x     |
|   Delux  |   75   |   100  |     x     |
|    VIP   |    x   |    x   |    200    |

### Additional requirement

Improvise. I listed a couple of base requirements. You can add whatever you feel necessary, and implement everything
however you feel comfortable.

### Suggestions

Feel free to solve your problems using google, even copy others' code, as long as you are sure that it works.

Some say that the main skill of a good software developer, is to be able to efficiently google a solutions.

