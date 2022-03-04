class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __eq__(self, other):
        if type(other) != Point:
            return False
        if other.x == self.x and other.y == self.y:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            if self.y > other.y:
                return True
        return False

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


p1 = Point(1, 2)
p2 = Point(2, 2)
p3 = Point(3, 1)
print(p1 == p2)
# False
print(p1 < p2)
# True
print(p1 > p2)
# False
print(p1 > p3)
# False
print(p1 < p3)
# True
print(p1 <= p3)
# True
print(p1 <= p1)
# True