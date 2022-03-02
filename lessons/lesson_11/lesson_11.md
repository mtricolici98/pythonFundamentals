# Classes Inheritance

Last lesson, we learned how to make classes.

Today, we're going to learn how to re-use classes and make new classes from old/existing classes.

# How does inheritance work.

Inheritance is the process when a class inherits the properties and methods of another class.

This means that the class that inherits the properties (the child class) has access to the same properties as the class
it inherited it from (the parent class).

Inheritance allows us to both reuse, and build on top of existing objects. Making it easier to add new features to
existing objects without modifying them.

Parent classes and Child classes are often called Base classes and Derived classes.

## Example

Say we have a class Animal.

Our animal class has properties such as name, age, species, weight.

And with methods such as "eat", "sleep"

Now we want to make a class specific for Dogs. The Dog class should contain all the same properties as the animal class,
but the species should be automatically set to "dog", and the added method of "bark".

We can solve this example by making two separate classes, and have the species property of Dog class to always be 'dog'.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} is eating')

    def sleep(self):
        print(f'{self.species} {self.name} is sleeping')


class Dog:

    def __init__(self, name):
        self.name = name
        self.species = 'dog'

    def eat(self):
        print(f'{self.species} {self.name} is eating')

    def sleep(self):
        print(f'{self.species} {self.name} is sleeping')

    def bark(self):
        print(f'{self.species} {self.name} is barking')
```

As you can see, this process is highly inefficient, especially when we need to add get and set methods. Because you will
have to copy them over from one to the other, when they are exactly the same.

## Using inheritance to simplify the process

In programming, we can use "inheritance" to solve this situation. We can have the Dog class inherit all properties from
our Animal class.

The process of inheriting a class is called "extending" that class.

Parent classes are declared inside the parenthesis of the child class.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} is eating')

    def sleep(self):
        print(f'{self.species} {self.name} is sleeping')


class Dog(Animal):  # Declaring animal as parent class

    def __init__(self, name):
        self.name = name
        self.species = 'Dog'

    def bark(self):
        print(f'{self.species} {self.name} is barking')


my_dog = Dog('Kuzea')
my_dog.eat()
# Dog Kuzea is eating
my_dog.sleep()
# Dog Kuzea is sleeping
my_dog.bark()
# Dog Kuzea is barking
```

We don't need to declare the .eat and .sleep methods for the Dog, because the class has automatically inherited them
from the Animal Class.

## What we have access to

Inside our Child (derived) classes we have access to all methods and properties of our Parent (base).

**Dog class has access to eat and sleep but also bark.**

Parent classes have access only to properties that it declares.

**Animal class has access only access to eat and sleep methods, and it can't access the bark method of its child class**

For example, if we have a property "breed" inside our Dog class, the Animal class has no way to access it.

## Overwriting methods

Overwriting is the process in which we implement a method of our parent class inside our child class. By doing this,
"overwrite" the parent method in our child class.

Overwriting is done by declaring the same method as the parent class.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} is eating')

    def sleep(self):
        print(f'{self.species} {self.name} is sleeping')


class Dog(Animal):  # Declaring animal as parent class

    def __init__(self, name, breed):
        self.name = name
        self.species = 'Dog'
        self.breed = breed

    def eat(self):  # We overwrite the eat method of Animal class with our own
        # This method uses the breed instead of the species 
        print(f'{self.breed} {self.name} is eating')

    def bark(self):
        print(f'{self.breed} {self.name} is barking')
```

In the example above, we have overwritten the .eat method for the Dog class. This new method is only available for the
Dog class. The original method in the Animal class is left untouched.

```python
animal = Animal('Patrick', 'star')
animal.eat()
# star Patrick is eating
dog = Dog('Tuzea', 'puddle')
dog.eat()
# puddle Tuzea is eating
```

# Accessing parent methods.

Sometimes we want to add functionality over existing functionality. It will also be very inefficient to re-implement the
functionality of our parent class in order to improve it.

For this reason, we have the ability to access our parents methods from our child methods.

This is done using the **super()** function. The super function will return the insance of our parent class.

````python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f'{self.name} if eating'


class Dog(Animal):

    def __init__(self, name, breed):
        # We pass the arguments to our parent init function instead of
        # declaring the properties here
        super().__init__(name, 'dog')
        # We declare additional properties here
        self.breed = breed

    def eat(self):
        # We return value from our eat method, using another method from the parent class
        return f"Dog " + super().eat()


my_dog = Dog('Kuzea', 'puddle')
print(my_dog.eat())
# Dog Kuzea if eating

my_animal = Animal('Kuzea', 'Dog')
print(my_animal.eat())
# Kuzea if eating
````

If you want another example of working with inheritance, let's take a look at this.

```python
class Income:

    def __init__(self, money):
        self.money = money

    def value(self):
        return self.money


class TaxedIncome(Income):

    def __init__(self, money, tax_percent):
        super().__init__(money)
        self.tax_percent = tax_percent

    def total_tax(self):
        return super().value() * self.tax_percent / 100

    def value(self):
        return super().value() - self.total_tax()


print(Income(1000).value())
# 1000
print(TaxedIncome(1000, 20).value())
# 800.0
```

## Multiple inheritance

In python, we can inherit from multiple classes at the same time.

When doing that, the object will inherit all properties from both parent classes.

This introduces a small problem that we should be aware of. Only one of the common properties of both parent classes
will be applied to our child class.

Let me show you an example.

```python
class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Animal {self.name}'


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f'{self.name} is barking')

    def __str__(self):
        return f'Dog {self.name}'


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f'{self.name} is meowing')

    def __str__(self):
        return f'Cat {self.name}'


class CatDog(Cat, Dog):

    def __init__(self, name):
        super().__init__(name)


catdog = CatDog('Meowdog')
print(catdog)
# Cat Meowdog -- The __str__ method of cat was used.
catdog.meow()
# Meowdog is meowing
catdog.bark()
# Meowdog is barking
```

As you can see above, we can use both methods from our Cat and from our Dog class inside our CatDog class. But
the `__str__` method is only used from one of the parent classes.

This is because python has a specific order for how functions should be attempted to be called.

It is called Multiple-resolution order (MRO). The MRO is what decides which methods are used in case more than one of
the classes in the hierarchy have declared the same method.

```python
print(CatDog.mro())
# [<class '__main__.CatDog'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
```

The list printed above shows the order in which python will try to call a method/property.

Python will try to find the property on in order in each of the classes, and if it doesn't it moves to the next class.

````python
class A:
    def __init__(self):
        print('A Init')


class B:
    def __init__(self):
        print('B Init')


class C(B, A):
    def __init__(self):
        print('C Init')
        super().__init__()


C()
# C Init
# B Init
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
````

### How can we explicitly tell which one to use ?

Although we shouldn't do it, we can do it in a very wierd way.

We can call the method inside the function manually, disregarding inheritance.

For example:

```python
class Foo:
    def funct(self, arg):
        print(f'Foo {arg}')


class Bar:
    def funct(self, arg):
        print(f'Bar {arg}')


class FooBar(Foo, Bar):

    def funct_foo(self, arg):
        Foo.funct(self, arg)

    def funct_bar(self, arg):
        Bar.funct(self, arg)


foo_bar = FooBar()
foo_bar.funct_bar('Test')
# Bar Test
foo_bar.funct_foo('Test')
# Foo Test
print(FooBar.mro())
# [<class '__main__.FooBar'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>]
foo_bar.funct('Test')
# Foo Test
```

## Checking the parent of an object

We have discovered the **type** that lets us know what is the direct type of an object. How can we find out if a object
is part of a hierarchy ?

There are 2 methods:

`isintance` - Returns and `issubclass`

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass


c_instance = C()

print(isinstance(c_instance, C))
# True
print(isinstance(c_instance, B))
# True
print(isinstance(c_instance, A))
# True

# Checks if C is a subclass of A
print(issubclass(C, A))
# True

# Checks if A is a subclass of C
print(issubclass(A, C))
# False

```

## Best practices for multiple inheritance

Multiple inheritance is not common in a lot of programming languages, and that's for a good reason. As we have seen
above, a lot of "questions" begin to appear when you allow a class to inherit from multiple places.

It is best not to use multiple inheritance unless you really need it.

When you use it, it's very important to be aware of the properties your objects posses, and avoid situations where both
parents share properties or methods. Because this can and will cause problems.

## Example multiple inheritance

Remember the homework we had for the previous lesson ? Let's update it to use inheritance.

We are going to create a Pet Class and a Human Class, and then we are going to create a PetOwner class and a
HumanWithPet class.

```python
class Pet:

    def __init__(self, name, type, fav_food):
        self.name = name
        self.type = type
        self.fav_food = fav_food

    def __str__(self):
        return f"{self.type.capitalize()} called {self.name} that loves {self.fav_food}"


class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()}, age {self.age}"


class PetOwner:

    def __init__(self, list_of_pets=None):
        self.list_of_pets = list_of_pets or []

    def adopt_pet(self, pet: Pet):
        self.list_of_pets.append(pet)

    def give_away_pet(self, pet: Pet):
        self.list_of_pets.remove(pet)


class HumanWithPet(Human, PetOwner):

    def __init__(self, first_name, last_name, age, initial_pets):
        super().__init__(first_name, last_name, age)
        PetOwner.__init__(self, initial_pets)

    def __str__(self):
        pet_count = len(self.list_of_pets)
        pet_string = "no pets."
        if pet_count > 1:
            pet_string = f"{pet_count} pets:"
        elif pet_count == 1:
            pet_string = f"{pet_count} pet:"
        pet_list = ", ".join([str(pet) for pet in self.list_of_pets])
        return f"{super().__str__()} has {pet_string} {pet_list}"


pet_1 = Pet('Garfield', "Cat", "Lasagna")
pet_2 = Pet('Winnie', "Bear", "Honey")
human = HumanWithPet('Marius', 'Tricolici', 21, [pet_1, pet_2])
print(pet_1)
# Cat called Garfield that loves Lasagna
print(pet_2)
# Bear called Winnie that loves Honey
print(human)
# Marius Tricolici, age 21 has 2 pets: Cat called Garfield that loves Lasagna, Bear called Winnie that loves Honey
```