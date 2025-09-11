from math import gcd

class Rational:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            n, d = map(int, args[0].split('/'))
        elif len(args) == 2:
            n, d = args
        elif len(args) == 1 and isinstance(args[0], Rational):
            n, d = args[0].n, args[0].d
        else:
            raise ValueError("Invalid constructor arguments")

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        common = gcd(n, d)
        self.n = n // common
        self.d = d // common
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            num = self.n * other.d + other.n * self.d
            den = self.d * other.d
            return Rational(num, den)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            num = self.n * other.d - other.n * self.d
            den = self.d * other.d
            return Rational(num, den)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            other = Rational(other, 1)
        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError("Division by zero")
            return Rational(self.n * other.d, self.d * other.n)
        return NotImplemented

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Key must be 'n' or 'd'")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.d = value
        else:
            raise KeyError("Key must be 'n' or 'd'")
        self._reduce()

    def _reduce(self):
        common = gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d


def parse_token(token):
    token = token.strip()
    if '/' in token:
        return Rational(token)
    else:
        return int(token)

def evaluate_expression(expression):
    tokens = expression.replace('*', ' * ').replace('-', ' - ').replace('+', ' + ').replace('/', ' / ').split()
    result = parse_token(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_val = parse_token(tokens[i + 1])
        if op == '+':
            result = result + next_val
        elif op == '-':
            result = result - next_val
        elif op == '*':
            result = result * next_val
        elif op == '/':
            result = result / next_val
        else:
            raise ValueError(f"Unknown operator: {op}")
        i += 2
    return result

def main():
    try:
        with open("expressions.txt", "r") as file:
            for line in file:
                expression = line.strip()
                if not expression:
                    continue
                try:
                    result = evaluate_expression(expression)
                    print(f"Expression: {expression}")
                    print(f"Result (fraction): {result}")
                    print(f"Result (decimal): {result()}\n")
                except Exception as e:
                    print(f"Error evaluating expression '{expression}': {e}\n")
    except FileNotFoundError:
        print("File 'expressions.txt' not found.")

if __name__ == "__main__":
    main()
