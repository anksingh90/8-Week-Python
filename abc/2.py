# Overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return f"(self.i + x.i)i + (self.j + x.j)j + (self.k + x.k)k"

obj1 = Vector(1, 2, 3)
print(obj1)

obj2 = Vector(3, 4, 5)
print(obj2)

print(obj1 + obj2)

print(type(obj1))
print(type(obj2))