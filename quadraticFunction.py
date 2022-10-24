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
        else:
            print(f"Your function is:\n\n\t y = {self.a}x^2 + {self.b}x + {self.c} ")

    def get_x_when_y_0(self):
        pass

    def get_y_with_x(self):
        pass