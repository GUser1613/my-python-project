import math

class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(3, 4)
circle = Circle(5)
print(f"{rectangle.name}: площадь = {rectangle.area():.2f}, периметр = {rectangle.perimeter():.2f}")
print(f"{circle.name}: площадь = {circle.area():.2f}, периметр = {circle.perimeter():.2f}")
