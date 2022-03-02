class PetTypes:
    DOG = 'DOG'
    CAT = 'CAT'
    BIRD = 'BIRD'
    RODENT = 'RODENT'
    LIZARD = 'LIZARD'

    @staticmethod
    def get_all():
        return [PetTypes.DOG, PetTypes.CAT, PetTypes.BIRD, PetTypes.RODENT, PetTypes.LIZARD]

    @staticmethod
    def is_valid(type: str):
        return type.upper() in PetTypes.get_all()


class Pet:

    def __init__(self, name: str, type: str, favourite_food: str):
        self.name = name
        if not PetTypes.is_valid(type):
            raise Exception("not a valid pet type")
        self.type = type
        self.favourite_food = favourite_food

    def __str__(self):
        response = f"{self.type.capitalize()} called {self.name.capitalize()} that loves {self.favourite_food}"
        if self.type.upper() == PetTypes.DOG:
            response += '. Barf!'
        return response


if __name__ == "__main__":
    list = []
    while True:
        pet_name = input('Pet name:')
        pet_type = None
        while pet_type is None:
            pet_type_ = input(f'Input pet type: options: {PetTypes.get_all()}')
            if PetTypes.is_valid(pet_type_):
                pet_type = pet_type_.upper()
        fav_food = input(f'Input his favourit food')
        list.append(Pet(pet_name, pet_type, fav_food))
