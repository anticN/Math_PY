class LinearFunction:
    """
    This class allows the user to do operations with linear functions.
    It has the attributes a(slope) and (optional) b(y axial intercept).
    """
    def __init__(self):
        self.__a = float(input("Enter value for a: "))
        self.__b = float(input("Enter value for b: "))
        self.__lin_functions = []

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

    def lin_functions(self, i):
        return self.__lin_functions[i]

    def add_function(self):
        self.__lin_functions.append()

    def new_function(self):
        pass

    def print(self):
        if self.__b is None or self.__b == 0:
            print(f"Your function is:\n\ty = {self.__a}x")
        else:
            print(f"Your function is:\n\ty = {self.__a}x + {self.__b}")

    def get_x_when_y_0(self):
        y = 0
        y -= self.__b
        x = y / self.__a
        print(f"The x-coordinate is: {x} when y = 0")

    def get_y_with_x(self, x):
        y = self.__a*x+self.__b
        print(f"The y-value is: {y} when the x-value is: {x}")
