from dataclasses import dataclass


@dataclass
class Human:
    name: str
    country: str


@dataclass(init=True, eq=False)
class Car:
    model: str
    make: str


a = Human('Marius', 'Moldova')
b = Human('Andrei', 'Moldova')
c = Human('Marius', 'Moldova')
print(a == b)
print(a == c)
a = Car('Tesla', 'Model Y')
b = Car('Tesla', 'Model Y')
print(a == a)
print(a == b)
