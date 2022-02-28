class PowerTwo:
    power = 2

    def __init__(self, number, power=3):
        # if cusotm_power:
        #     self.power = cusotm_power
        self.value = number ** self.power

    def get_value(self):
        return self.value


la_patrat = PowerTwo(2)
print(la_patrat.get_value())

la_patrat = PowerTwo(2, 3)
print(la_patrat.get_value())

#
# la_patrat = PowerTwo(4)
# print(la_patrat.get_value())
#
# la_cub = PowerTwo(4)
# print(la_cub.get_value())
#
# la_cub = PowerTwo(4, 2)
# print(la_cub.get_value())
#
# la_cub = PowerTwo(4)
# print(la_cub.get_value())
