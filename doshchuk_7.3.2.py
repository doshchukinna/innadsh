class RationalValueError(Exception):
    def __init__(self, message="Некоректні дані для операції з раціональними числами"):
        self.message = message
        super().__init__(self.message)

class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise RationalValueError("Знаменник не може бути нулем")
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def add(self, other):
        if not isinstance(other, RationalNumber):
            raise RationalValueError("Операція підтримує тільки раціональні числа")
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def subtract(self, other):
        if not isinstance(other, RationalNumber):
            raise RationalValueError("Операція підтримує тільки раціональні числа")
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def multiply(self, other):
        if not isinstance(other, RationalNumber):
            raise RationalValueError("Операція підтримує тільки раціональні числа")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def divide(self, other):
        if not isinstance(other, RationalNumber):
            raise RationalValueError("Операція підтримує тільки раціональні числа")
        if other.numerator == 0:
            raise RationalValueError("Ділення на нуль не дозволяється")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return RationalNumber(new_numerator, new_denominator)


if __name__ == "__main__":
    try:
        a = RationalNumber(3, 4)
        b = RationalNumber(1, 2)
        result_add = a.add(b)
        print(f"Додавання: {result_add}")
        result_sub = a.subtract(b)
        print(f"Віднімання: {result_sub}")
        result_mul = a.multiply(b)
        print(f"Множення: {result_mul}")
        result_div = a.divide(b)
        print(f"Ділення: {result_div}")
        c = RationalNumber(0, 0)
        result_div_zero = a.divide(c)
    except RationalValueError as e:
        print(f"Помилка: {e}")
