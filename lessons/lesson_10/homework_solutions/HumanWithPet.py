from lessons.lesson_10.homework_solutions.Human import Human


class HumanWithPet:

    def __init__(self, first_name, last_name, date_of_birth, initial_pets):
        self.human = Human(first_name, last_name, date_of_birth)
        self.list_of_pets = initial_pets

    def __str__(self):
        pet_count = len(self.list_of_pets)
        pet_string = "no pets."
        if pet_count > 1:
            pet_string = f"{pet_count} pets:"
        elif pet_count == 1:
            pet_string = f"{pet_count} pet:"
        pet_list = ", ".join([str(pet) for pet in self.list_of_pets])
        return f"{str(self.human)} has {pet_string} {pet_list}"
