import os
import time
from linearFunction import LinearFunction
from quadraticFunction import QuadraticFunction
"""
@author Nikola Antic
@version 0.1
@since 2022-10-02
"""

if __name__ == '__main__':
    os.system("color")

    def get_point(func1, func2):
        xi = (lin_func.b - lin_func2.b) / (lin_func2.a - lin_func.a)
        yi = lin_func.a * xi + lin_func.b
        print(f"The intersection point of the two functions is: ({xi}|{yi})\n")

    def print_line():
        print("=================================================================")

    print(f"Hello {os.getlogin()}")
    print(f"Welcome to the Math-application written by Nikola Antic")
    print_line()
    #time.sleep(1)
    while True:
        print()
        print(f"What do you want to do with the programm?")
        user_choice = input(f"linear functions \033[1;32m(l/L)\033[0m, quadratic functions \033[1;32m(q/Q)\033[0m....")

        if user_choice == "l" or user_choice == "L":
            # The user creates a linear function and will be able to calculate with it
            lin_func = LinearFunction(float(input("Enter value for a(slope): ")),
                                float(input("Enter value for b(y axial intercept), if none just type 0: ")))
            lin_functions = []
            lin_functions.append(lin_func)
            print()
            lin_func.print()
            #time.sleep(1)
            print()
            while True:
                print()
                print("What do you want to do with the function?")
                print_line()
                lin_choice = input(f"Get the y-value with a x value\033[1;32m(y/Y)\033[0m.\nGet the x-value when y = 0\033[1;32m(x/X)\033[0m.\n"
                                   f"Add another function and get the point of intersection\033[1;32m(i/I)\033[0m.\n"
                                   f"Calculate with a new function\033[1;32m(n/N)\033[0m.\n"
                                   f"Exit the linear functions\033[1;32m(e/E)\033[0m.")
                if lin_choice == "y" or lin_choice == "Y":
                    # In this case the user enters a x-value and he will get the y-value.
                    lin_func.get_y_with_x(float(input(f"Type your x-value to get the y-value:")))
                    print()
                elif lin_choice == "x" or lin_choice == "X":
                    """
                    In this case the user will get the x-value when the y-value is 0
                    """
                    lin_func.get_x_when_y_0()
                    print()
                elif lin_choice == "i" or lin_choice == "I":
                    """
                    The user has to enter another linear function and he will get the point of intersection of the 
                    two functions
                    """
                    lin_func2 = LinearFunction(float(input("Enter value for a(slope): ")),
                                            float(input("Enter value for b(y axial intercept), if none just type 0: ")))
                    get_point(lin_func, lin_func2)
                elif lin_choice == "n" or lin_choice == "N":
                    """
                    The user can create a new function and calculate with it.
                    """
                    lin_func = LinearFunction(float(input("Enter value for a(slope): ")),
                                            float(input("Enter value for b(y axial intercept), if none just type 0: ")))
                    lin_func.print()
                elif lin_choice == "e" or lin_choice == "E":
                    break
        elif user_choice == "q" or user_choice == "Q":
            quad_func = QuadraticFunction(input("Enter value for a(slope): "), input("Enter value for b: "), input("Enter value for c(y axial intercept), if none just type 0: "))
            quad_func.print()

            while True:
                print()
