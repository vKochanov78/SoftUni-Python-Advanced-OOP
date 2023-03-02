class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, quantity) -> str:
        if self.content + quantity <= Glass.capacity:
            self.content += quantity
            return f"Glass filled with {quantity} ml"

        return f"Cannot add {quantity} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())