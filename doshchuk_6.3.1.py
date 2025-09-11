from math import gcd

class Rational:
    def __init__(self, a, b=1):
        if isinstance(a, str):
            a, b = map(int, a.split('/'))
        if b == 0:
            raise ZeroDivisionError
        g = gcd(a, b)
        a, b = a // g, b // g
        if b < 0:
            a, b = -a, -b
        self.n, self.d = a, b

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __radd__(self, other):
        return self + other

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n": return self.n
        if key == "d": return self.d
        raise KeyError

    def __setitem__(self, key, val):
        if key == "n": self.n = val
        elif key == "d":
            if val == 0: raise ZeroDivisionError
            self.d = val
        else: raise KeyError

class RationalList:
    def __init__(self):
        self.data = []

    def append(self, val):
        if isinstance(val, int):
            val = Rational(val)
        elif isinstance(val, str) or isinstance(val, Rational):
            val = Rational(val)
        self.data.append(val)

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, val):
        self.data[idx] = Rational(val)

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        new = RationalList()
        new.data = self.data.copy()
        if isinstance(other, RationalList):
            new.data += other.data
        else:
            new.append(other)
        return new

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data += other.data
        else:
            self.append(other)
        return self

    def __iter__(self):
        return iter(sorted(self.data, key=lambda x: (-x.d, -x.n)))

    def sum(self):
        return sum(self.data, Rational(0))

def read_file(filename):
    rlist = RationalList()
    with open(filename) as f:
        for line in f:
            for val in line.split():
                try:
                    rlist.append(val)
                except: pass
    return rlist

def main():
    rlist = read_file("numbers.txt")
    for r in rlist:
        print(r)

if __name__ == "__main__":
    main()
