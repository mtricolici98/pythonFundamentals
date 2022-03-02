from datetime import date, datetime

from lessons.lesson_10.homework_solutions.HumanWithPet import HumanWithPet
from lessons.lesson_10.homework_solutions.Pet import Pet

pet_1 = Pet('Garfield', "Cat", "Lasagna")
pet_2 = Pet('Winnie', "Bear", "Honey")
human = HumanWithPet('Marius', 'Tricolici', date(2000, 3, 2), [pet_1, pet_2])

print(datetime.now().date())
print(date(2000, 3, 1))

print(pet_1)

print(pet_2)

print(human)
