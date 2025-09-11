import math

class Triangle:
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError("Це не трикутник. Сума двох сторін повинна бути більшою за третю.")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Сторони прямокутника повинні бути позитивними числами.")
        self.width, self.height = width, height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Trapeze:
    def __init__(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError("Довжини сторін трапеції повинні бути позитивними числами.")
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self, height):
        if height <= 0:
            raise ValueError("Висота трапеції повинна бути позитивним числом.")
        return (self.a + self.b) * height / 2

class Parallelogram:
    def __init__(self, a, b, height):
        if a <= 0 or b <= 0 or height <= 0:
            raise ValueError("Сторони та висота паралелограма повинні бути позитивними числами.")
        self.a, self.b, self.height = a, b, height

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.height

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радіус кола повинен бути позитивним числом.")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

def read_figures(file_name):
    figures = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 2:
                continue
            figure_type = parts[0]
            try:
                parameters = list(map(float, parts[1:]))
                if figure_type == "Triangle" and len(parameters) == 3:
                    figures.append(Triangle(*parameters))
                elif figure_type == "Rectangle" and len(parameters) == 2:
                    figures.append(Rectangle(*parameters))
                elif figure_type == "Trapeze" and len(parameters) == 4:
                    figures.append(Trapeze(*parameters))
                elif figure_type == "Parallelogram" and len(parameters) == 3:
                    figures.append(Parallelogram(*parameters))
                elif figure_type == "Circle" and len(parameters) == 1:
                    figures.append(Circle(*parameters))
                else:
                    print(f"Невірні параметри для фігури: {figure_type}")
            except ValueError as e:
                print(f"Помилка при обробці фігури: {e}")
    return figures

def find_largest_area_and_perimeter(figures):
    max_area = 0
    max_area_figure = None
    max_perimeter = 0
    max_perimeter_figure = None

    for figure in figures:
        try:
            area = figure.area()
            perimeter = figure.perimeter()
            if area > max_area:
                max_area = area
                max_area_figure = figure
            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_perimeter_figure = figure
        except ValueError as e:
            print(f"Помилка при обчисленні для фігури: {e}")

    return max_area_figure, max_area, max_perimeter_figure, max_perimeter

if __name__ == "__main__":
    try:
        figures = read_figures("figures.txt")
        if not figures:
            print("Не знайдено жодної фігури для обробки.")
        else:
            max_area_figure, max_area, max_perimeter_figure, max_perimeter = find_largest_area_and_perimeter(figures)

            if max_area_figure:
                print(f"Фігура з найбільшою площею: {max_area_figure.__class__.__name__}, площа: {max_area}")
            if max_perimeter_figure:
                print(f"Фігура з найбільшим периметром: {max_perimeter_figure.__class__.__name__}, периметр: {max_perimeter}")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
