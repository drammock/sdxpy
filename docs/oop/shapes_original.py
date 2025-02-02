import math

# [shape]
class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")
# [/shape]

# [concrete]
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2
# [/concrete]

# [poly]
examples = [Square("sq", 3), Circle("ci", 2)]
for ex in examples:
    n = ex.name
    p = ex.perimeter()
    a = ex.area()
    c = ex.__class__.__name__
    print(f"{n} is a {c} {p:.2f} {p:.2f}")
# [/poly]
