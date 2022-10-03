class QuadraticFunction:
    """
    This class describes a quadratic function with the attributes a(slope), b and c (y axial intercept)
    """
    def __init__(self, a, b, c):
        self.__a = float(input("Enter value for a(slope): "))
        self.__b = float(input("Enter value for b: "))
        self.__c = float(input("Enter value for b(y axial intercept), if none just type 0: "))

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
        pass

    def get_x_when_y_0(self):
        pass

    def get_y_with_x(self):
        pass