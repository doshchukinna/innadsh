import math

class RationalValueError(Exception):
    pass

class Rational:
    def __init__(self, *args):
        if len(args) == 2:
            self.n = args[0]
            self.d = args[1]
            if self.d == 0:
                raise RationalValueError("Знаменник не може бути нулем!")
            self.simplify()
        elif len(args) == 1:
            fraction = args[0].split('/')
            if len(fraction) != 2:
                raise RationalValueError("Невірний формат дробу!")
            self.n = int(fraction[0])
            self.d = int(fraction[1])
            if self.d == 0:
                raise RationalValueError("Знаменник не може бути нулем!")
            self.simplify()
        else:
            raise RationalValueError("Невірна кількість аргументів!")

    def simplify(self):
        gcd = math.gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __add__(self, other):
        if isinstance(other, Rational):
            new_n = self.n * other.d + self.d * other.n
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n + self.d * other
            new_d = self.d
        else:
            raise RationalValueError("Не підтримується операція для даного типу.")
        return Rational(new_n, new_d)

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_n = self.n * other.d - self.d * other.n
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n - self.d * other
            new_d = self.d
        else:
            raise RationalValueError("Не підтримується операція для даного типу.")
        return Rational(new_n, new_d)

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_n = self.n * other.n
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n * other
            new_d = self.d
        else:
            raise RationalValueError("Не підтримується операція для даного типу.")
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_n = self.n * other.d
            new_d = self.d * other.n
        elif isinstance(other, int):
            new_n = self.n
            new_d = self.d * other
        else:
            raise RationalValueError("Не підтримується операція для даного типу.")
        return Rational(new_n, new_d)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Недопустимий ключ! Використовуйте 'n' або 'd'.")

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"

if __name__ == "__main__":
    try:
        r1 = Rational(3, 4)
        r2 = Rational("5/6")
        print(r1 + r2)
        print(r1 - r2)
        print(r1 * r2)
        print(r1 / r2)
        print(r1())
        print(r1["n"])
        print(r1["d"])
    except RationalValueError as e:
        print(e)
