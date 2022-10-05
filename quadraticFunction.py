class QuadraticFunction:
    """
    This class describes a quadratic function with the attributes a(slope), b and c (y axial intercept)
    """
    def __init__(self, a, b, c):
        #self.__a = float(input("Enter value for a(slope): "))
        #self.__b = float(input("Enter value for b: "))
        #self.__c = float(input("Enter value for b(y axial intercept), if none just type 0: "))
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        """
        Getter function for a value.
        :return: a
        """
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def print(self):
        pass

    def get_x_when_y_0(self):
        pass

    def get_y_with_x(self):
        pass