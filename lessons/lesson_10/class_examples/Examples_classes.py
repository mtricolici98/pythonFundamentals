class Animal:

    def __init__(self, name, species=None):
        self.name = name
        self.species = species


class Dog:
    species = 'Dog'

    def __init__(self, name):
        self.name = name


my_dog = Dog('Kuzea')

print(my_dog.species)
