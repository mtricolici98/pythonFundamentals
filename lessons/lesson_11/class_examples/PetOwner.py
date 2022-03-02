from classes_2.Pet import Pet


class PetOwner:

    def __init__(self, list_of_pets=None):
        self.list_of_pets = list_of_pets or []

    def adopt_new_pet(self, pet: Pet):
        self.list_of_pets.append(pet)

    def give_away_pet(self, pet: Pet):
        self.list_of_pets.remove(pet)
