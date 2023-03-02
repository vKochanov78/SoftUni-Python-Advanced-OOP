class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x_value):
        self.x = new_x_value

    def set_y(self, new_y_value):
        self.y = new_y_value

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)