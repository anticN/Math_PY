class LinearFunction:
    """
    This class represents linear functions and allows the user to operate with them.
    It has the attributes a(slope) and (optional) b(y axial intercept).
    """
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

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

    def print(self):
        """
        Depending on the values the programm will print other statements.
        """
        if self.__b is None or self.__b == 0:
            print(f"Your function is:\n\n\ty = {self.__a}x")
        elif self.__b < 0:
            print(f"Your function is: \n\n\ty = {self.__a}x - {self.__b/-1}")
        elif self.__a < 0:
            print(f"Your function is: \n\n\ty = -{self.__a / -1}x + {self.__b}")
        elif self.__a < 0 and self.__b < 0:
            print(f"Your function is: \n\n\ty = -{self.__a / -1}x - {self.__b / -1}")
        else:
            print(f"Your function is:\n\n\ty = {self.__a}x + {self.__b}")

    def get_x_when_y_0(self):
        y = 0
        y -= self.__b
        x = y / self.__a
        print(f"The x-value is: {x} when y = 0")

    def get_y_with_x(self, x):
        y = self.__a*x+self.__b
        print(f"\nThe y-value is: {y} when the x-value is: {x}")


