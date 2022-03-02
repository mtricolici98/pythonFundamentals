from datetime import date

from classes_2.Human import Human
from classes_2.Pet import Pet, PetTypes
from classes_2.PetOwner import PetOwner


class HumanWithPet(Human, PetOwner):

    def __init__(self, first_name, last_name, date_of_birth, initial_list_of_pets):
        super().__init__(first_name, last_name, date_of_birth)
        PetOwner.__init__(self, initial_list_of_pets)

    def __str__(self):
        human_str = super().__str__()
        pet_str = 'no pets.'
        if len(self.list_of_pets) == 1:
            pet_str = f'one pet: {str(self.list_of_pets[0])}'
        elif len(self.list_of_pets) > 1:
            str_of_pets = ", ".join([str(pet) for pet in self.list_of_pets])
            pet_str = f'{len(self.list_of_pets)} pets: {str_of_pets}'
        return f"{human_str} has {pet_str}"


pet_1 = Pet('Kuzea', PetTypes.DOG, 'Bone')
pet_2 = Pet('Baghira', PetTypes.CAT, 'Fish')
hwp = HumanWithPet('Marius', 'Tricolici', date(2000, 1, 19), initial_list_of_pets=[])
print(hwp)
hwp2 = HumanWithPet('Marius', 'Tricolici', date(2000, 1, 19), initial_list_of_pets=[pet_1])
print(hwp2)
hwp3 = HumanWithPet('Marius', 'Tricolici', date(2000, 1, 19), initial_list_of_pets=[pet_1, pet_2])
print(hwp3)
hwp3.give_away_pet(pet_1)
print(hwp3)
