import math
import time


class QuadraticFunction:
    """
    This class describes a quadratic function with the attributes a(slope), b and c (y axial intercept)
    """
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def print(self):
        if self.b == 0 and self.c == 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2")
        elif self.b == 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2 + {self.c}")
        elif self.c == 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2 + {self.b}x")
            #muss prüfen
        elif self.a < 0 and self.b < 0 and self.c < 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 - {self.b/-1}x - {self.c/-1}")
        elif self.a < 0 and self.b < 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 - {self.b/-1}x + {self.c}")
        elif self.a < 0 and self.c < 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 + {self.b}x - {self.c/-1}")
        elif self.b < 0 and self.c < 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2 - {self.b/-1}x - {self.c/-1}")
        elif self.a < 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 + {self.b}x + {self.c}")
        elif self.b < 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2 - {self.b/-1}x + {self.c}")
        elif self.c < 0:
            print(f"Your function is:\n\n\t y = {self.a}x^2 + {self.b}x - {self.c/-1}")
        elif self.a < 0 and self.b < 0 and self.c == 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 - {self.b/-1}x")
        elif self.a < 0 and self.c < 0 and self.b == 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2 - {self.c/-1}")
        elif self.a < 0 and self.b == 0 and self.c == 0:
            print(f"Your function is:\n\n\t y = -{self.a/-1}x^2")
        else:
            print(f"Your function is:\n\n\t y = {self.a}x^2 + {self.b}x + {self.c} ")
        time.sleep(1)

    def get_x_when_y_0(self):
        d = self.b * self.b - (4 * self.a * self.c)
        if d < 0:
            print(f"This function doesn't have points on the x-axis")
        else:
            x1 = (self.b / -1 + math.sqrt(d)) / (2 * self.a)
            x2 = (self.b / -1 - math.sqrt(d)) / (2 * self.a)
            print(f"\nThe null-points of this function are at the x-coordinates {x1} and {x2}")

    def get_y_with_x(self, x):
        y = float((self.a * x * x) + (self.b * x) + self.c)
        print(f"\nThe y-value is: {y} when the x-value is: {x}")

    def vertex(self):
        sx = (self.b / (2 * self.a)) / -1
        sy = self.c - (self.b * self.b / (4 * self.a))
        print(f"\nThe vertex is located at ({sx}|{sy})")

