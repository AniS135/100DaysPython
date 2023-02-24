class Shape:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__(self.radius, self.radius)
    
    def area(self):
        return 3.14 * super().area()

rec = Shape(3, 5)
print(rec.area())

c = Circle(5)
print(c.area())