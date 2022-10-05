class LinearFunction:
    """
    This class represents linear functions and allows the user to operate with them.
    It has the attributes a (slope) and (optional) b(y axial intercept).
    """
    def __init__(self, a, b):
        try:
            self.__a = a
            self.__b = b
        except WrongDatatypeException:
            print("Please enter a valid datatype.")

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def print(self):
        if self.__b is None or self.__b == 0:
            print(f"Your function is:\n\ty = {self.__a}x\n")
        else:
            print(f"Your function is:\n\ty = {self.__a}x + {self.__b}\n")

    def get_x_when_y_0(self):
        y = 0
        y -= self.__b
        x = y / float(self.__a)
        print(f"The x-coordinate is: {x} when y = 0\n")

    def get_y_with_x(self, x):
        y = self.__a*x+self.__b
        print(f"The y-value is: {y} when the x-value is: {x}\n")

    def get_point_of_intersection(self, func2):
        pass


class WrongDatatypeException(Exception):
    def __init__(self, message):
        super().__init__(message)
