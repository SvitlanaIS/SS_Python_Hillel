# Variant 1
class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.n = n
        self.d = d

    def __mul__(self, other):
        new_num = self.n * other.n
        new_den = self.d * other.d
        return Fraction(new_num, new_den)

    def __add__(self, other):
        new_num = self.n * other.d + other.n * self.d
        new_den = self.d * other.d
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.n * other.d - other.n * self.d
        new_den = self.d * other.d
        if new_num <= 0:
            raise ValueError("Результат віднімання не є правильним дробом")
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.n * other.d == self.n * other.d

    def __gt__(self, other):
        return self.n * other.d > self.d * other.n

    def __lt__(self, other):
        return self.n * other.d < self.d * other.n

    def __ne__(self, other):
        return self.n * other.d != self.d * other.n

    def __str__(self):
        return f"Fraction: {self.n}, {self.d}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')


# Variant 2
import math
class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Знаменник не може бути нулем")
        if n <= 0 or n >= d:
             raise ValueError("Це неправильний дріб: чисельник має бути > 0 та < знаменника.")
        gcd = math.gcd(n,  d)
        self.n = n // gcd
        self.d = d // gcd

    def __mul__(self, other):
        new_num = self.n * other.n
        new_den = self.d * other.d
        return Fraction(new_num, new_den)

    def __add__(self, other):
        new_num = self.n * other.d + other.n * self.d
        new_den = self.d * other.d
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.n * other.d - other.n * self.d
        new_den = self.d * other.d
        if new_num <= 0:
            raise ValueError("Результат віднімання не є правильним дробом")
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.n * other.d == self.n * other.d

    def __gt__(self, other):
        return self.n * other.d > self.d * other.n

    def __lt__(self, other):
        return self.n * other.d < self.d * other.n

    def __ne__(self, other):
        return self.n * other.d != self.d * other.n

    def __str__(self):
        return f"{self.n}/{self.d}"

f_a = Fraction(1, 3)
f_b = Fraction(1, 6)
f_c = f_b + f_a
assert str(f_c) == '1/2'
f_d = f_b * f_a
assert str(f_d) == '1/18'
f_e = f_a - f_b
assert str(f_e) == '1/6'

assert f_d < f_c  # True
assert f_e > f_d  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
