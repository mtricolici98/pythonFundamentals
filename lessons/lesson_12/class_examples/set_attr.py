class ImmutablePoint:
    _locked = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._locked = True

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __setattr__(self, key, value):
        if self._locked:
            raise Exception(f'Object is immutable, modifications are not allowed')
        super().__setattr__(key, value)


p1 = ImmutablePoint(4, 2)
print(p1.x)
# 2
print(p1.y)
# 3
p1.x
p1.y = 1
print(p1)
# Exception: Object is immutable, modifications are not allowed
