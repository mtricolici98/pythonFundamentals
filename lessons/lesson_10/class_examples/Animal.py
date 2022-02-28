class Animal:
    name = None

    def set_name(self, name):
        self.name = name


new_animal = Animal()
new_animal.set_name('Kuzea')

another_animal = Animal()
another_animal.set_name('Tuzea')

another_animal.name = 'Barsik'

print(new_animal)
print(another_animal)
print(new_animal)
