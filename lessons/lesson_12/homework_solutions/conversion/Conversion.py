class Conversion:

    def __init__(self, from_curr, to_curr, name, rate, date, inverseRate):
        self.from_curr = from_curr
        self.to_curr = to_curr
        self.name = name
        self.rate = rate
        self.date = date
        self.inverseRate = inverseRate

    @classmethod
    def from_dict(cls, dict_data, from_currency):
        return cls(
            from_currency,
            dict_data['code'],
            dict_data['name'],
            dict_data['rate'],
            dict_data['date'],
            dict_data['inverseRate'],
        )

    def __str__(self):
        return f"Conversion from {self.from_curr} to {self.to_curr} at rate {self.rate}"

    def __gt__(self, other):
        if isinstance(other, Conversion):
            return self.rate > other.rate
        raise TypeError("Not comparing to a Conversion")

    def __lt__(self, other):
        if isinstance(other, Conversion):
            return self.rate < other.rate
        raise TypeError("Not comparing to a Conversion")

    def __eq__(self, other):
        if isinstance(other, Conversion):
            return self.rate == other.rate
        raise TypeError("Not comparing to a Conversion")

    def __le__(self, other):
        if isinstance(other, Conversion):
            return self.rate <= other.rate
        raise TypeError("Not comparing to a Conversion")

    def __ge__(self, other):
        if isinstance(other, Conversion):
            return self.rate >= other.rate
        raise TypeError("Not comparing to a Conversion")
