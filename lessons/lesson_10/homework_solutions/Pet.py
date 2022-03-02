class Pet:

    def __init__(self, name, type, fav_food):
        self.name = name
        self.type = type
        self.fav_food = fav_food

    def __str__(self):
        return f"{self.type.capitalize()} called {self.name} that loves {self.fav_food}"
