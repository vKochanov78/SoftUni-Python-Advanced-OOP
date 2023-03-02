class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius_value):
        self.radius = new_radius_value

    def get_area(self) -> float:
        return round((self.pi * self.radius ** 2), 2)

    def get_circumference(self) -> float:
        return round((2 * self.pi * self.radius), 2)


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())