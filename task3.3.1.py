import math

class Figure:
    def dimension(self):
        raise NotImplementedError()

    def perimeter(self):
        return None

    def square(self):
        return None

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        return None

    def volume(self):
        if self.dimension() == 2:
            return self.square()
        else:
            return None

    def measure(self):
        if self.dimension() == 2:
            return self.square()
        else:
            return self.volume()

    def __str__(self):
        return self.__class__.__name__

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

class Trapeze(Figure):
    def __init__(self, a, b, c, d, h):
        self.a, self.b, self.c, self.d, self.h = a, b, c, d, h

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return (self.a + self.b) * self.h / 2

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def volume(self):
        return 4/3 * math.pi * self.r ** 3

    def square_surface(self):
        return 4 * math.pi * self.r ** 2

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return 3

    def square_base(self):
        return super().square()

    def square_surface(self):
        l = math.sqrt((self.a/2)**2 + self.h**2)
        return self.square_base() + 3 * (self.a * l / 2)

    def height(self):
        return self.h

    def volume(self):
        return self.square_base() * self.h / 3

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimension(self):
        return 3

    def square_base(self):
        return super().square()

    def square_surface(self):
        l1 = math.sqrt((self.a/2)**2 + self.h**2)
        l2 = math.sqrt((self.b/2)**2 + self.h**2)
        return self.square_base() + self.a * l1 + self.b * l2

    def height(self):
        return self.h

    def volume(self):
        return self.square_base() * self.h / 3

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def square_surface(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimension(self):
        return 3

    def square_base(self):
        return super().square()

    def square_surface(self):
        l = math.sqrt(self.r**2 + self.h**2)
        return math.pi * self.r * (self.r + l)

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * super().square() * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return 3

    def square_base(self):
        return super().square()

    def square_surface(self):
        return 2 * self.square_base() + self.perimeter() * self.h

    def height(self):
        return self.h

    def volume(self):
        return self.square_base() * self.h

def create_figure(name, params):
    params = list(map(float, params))
    match name:
        case "Triangle":
            return Triangle(*params)
        case "Rectangle":
            return Rectangle(*params)
        case "Trapeze":
            return Trapeze(*params)
        case "Parallelogram":
            return Parallelogram(*params)
        case "Circle":
            return Circle(*params)
        case "Ball":
            return Ball(*params)
        case "TriangularPyramid":
            return TriangularPyramid(*params)
        case "QuadrangularPyramid":
            return QuadrangularPyramid(*params)
        case "RectangularParallelepiped":
            return RectangularParallelepiped(*params)
        case "Cone":
            return Cone(*params)
        case "TriangularPrism":
            return TriangularPrism(*params)
        case _:
            raise ValueError(f"Unknown figure: {name}")

def main():
    figures = []

    with open("figures.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            name = parts[0]
            params = parts[1:]
            figure = create_figure(name, params)
            figures.append(figure)

    max_figure = max(figures, key=lambda fig: fig.measure())

    print(f"Фігура з найбільшою мірою: {max_figure}")
    print(f"Її міра: {max_figure.measure():.2f}")

if __name__ == "__main__":
    main()
