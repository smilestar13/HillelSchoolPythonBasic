class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return not self > other
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


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
