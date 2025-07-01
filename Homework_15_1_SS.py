import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
       return self.get_square() == other.get_square()

    def __add__(self, other):
        total_square = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_square / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("Множник має бути позитивним числом")
        multiplier = math.sqrt(n)
        new_width = self.width * multiplier
        new_height = self.height * multiplier
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Прямокутник: {self.width:.2f} x {self.height:.2f}, площа = {self.get_square():.2f}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
print(r1)
print(r2)

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print(r3)

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'