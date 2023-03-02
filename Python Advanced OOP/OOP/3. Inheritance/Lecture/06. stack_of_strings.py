from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


obj = Stack()
obj.push("Dog")
obj.push("Cat")
obj.push("Parrot")
print(f"List: {obj.data}")
print(f"Pop: {obj.pop()}")
print(f"Top: {obj.top()}")
print(f"is_empty: {obj.is_empty()}")
print(obj.__str__())