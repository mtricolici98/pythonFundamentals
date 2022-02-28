# Homework

## Testing the exercises.

To test your classes, create test functions that will execute all the methods that you have added to your classes.

Each of your classes should be defined in separate files, that have the same name as the name of the Class.

Example class Human should be in Human.py file.

## Ex 1

Create a class that describes a human.

Human object should have the following properties:

* First Name - string
* Last Name - string
* Date of Birth - datetime.date

All the properties above should be initialized in the constructor function, by arguments to the constructor.

And the following methods:

* A method to get the full name of the human
* A method to get the age of the human

When printing the human object the console should output something like example below:

`Marius Tricolici, age 24`

## Ex 2

Create a class that describes a pet.

A pet should have the following properties:

* A name - string
* A type (cat/dog/bird) - string
* A favourite food - string

All the properties above should be initialized in the constructor function, by arguments to the constructor.

When a pet object is printed it should output something like this:

`Cat called Garfield that loves lasagna`
or
`Dog called Kuzea that loves bones`

Also create a new class HumanWithPet:

The HumanWithPet should have the same properties as the Human in [Ex 1](#ex-1).

Additionally, the HumanWithPet class should have a list of pets as a property.

Add two methods to the HumanWithPet class:

* Adopt new pet - Adds a new pet object to the list of pets
* Give away pet - Removes a pet from the humans list of pets

When printing a HumanWithPet object, the console should output the according to the following examples:

`Marius Tricolici, age 24 with a pet: Cat called Garfield that loves lasagna` - If the human has 1 pets.

`Marius Tricolici, age 24 with 2 pets: Cat called Garfield that loves lasagna, Dog called Kuzea that loves bones` - If
the human has 2 or more pets.


### Want more ? Let me know :) 