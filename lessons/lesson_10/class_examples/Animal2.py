class Animal:
    name = None
    species = None

    def __init__(self, name, species=None):
        self.name = name
        if not species:
            print('No species')
        self.species = species


my_object = Animal('Kuzea')