import random

class Dice:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.last_roll_value = None
        self.roll_history = []

    def roll(self):
        roll_number = random.randint(1, self.number_of_sides)
        self.roll_history.append(roll_number)
        self.last_roll_value = roll_number

    def last_roll(self):
        return self.last_roll_value

    def get_rol_history(self):
        return self.roll_history


class DiceSet:

    def __init__(self, sides_per_dice, number_of_dices=2):
        self.sides_per_dice = sides_per_dice
        self.list_of_dice = [Dice(sides_per_dice) for a in range(number_of_dices)]
        self.roll_history = []
        self._rigged_rolls_history = []

    def roll_all(self):
        results = []
        for dice in self.list_of_dice:
            dice.roll()
            results.append(dice.last_roll())
        self.roll_history.append(results)
        return sum(results)


dice_set_of_2 = DiceSet(6, 2)
print(dice_set_of_2.roll_all())
print(dice_set_of_2.roll_all())
print(dice_set_of_2.roll_all())
print(dice_set_of_2.roll_all())

