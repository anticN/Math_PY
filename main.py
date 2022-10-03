import os
import time
from linearFunction import LinearFunction
"""
@author Nikola Antic
@version 0.1
@since 2022-10-02
"""

if __name__ == '__main__':
    print(f"Hello {os.getlogin()}")

    def print_line():
        print("=================================================================")

    print(f"Welcome to the Math-application written by Nikola Antic")
    print_line()
    time.sleep(1)
    while True:
        print()
        print(f"What do you want to do with the programm?")
        user_choice = input(f"linear functions \033[1;32m(l/L)\033[0m, quadratic functions \033[1;32m(q/Q)\033[0m....")

        if user_choice == "l" or user_choice == "L":
            lin_func = LinearFunction()
            lin_functions = []
            lin_functions.append(lin_func)
            print()
            lin_func.print()
            time.sleep(1)
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
                    lin_func.get_y_with_x(float(input(f"Type your x-value to get the y-value:")))
                    print()
                elif lin_choice == "x" or lin_choice == "X":
                    lin_func.get_x_when_y_0()
                    print()
                elif lin_choice == "i" or lin_choice == "I":
                    lin_func2 = LinearFunction()

                    def get_point(func1, func2):
                        xi = (lin_func.b - lin_func2.b) / (lin_func2.a - lin_func.a)
                        yi = lin_func.a * xi + lin_func.b
                        print(f"The intersection point of the two functions is: ({xi}|{yi})")
                        print()

                    get_point(lin_func, lin_func2)
                elif lin_choice == "n" or lin_choice == "N":
                    lin_func = LinearFunction()
                    lin_func.print()
                elif lin_choice == "e" or lin_choice == "E":
                    break
        elif user_choice == "q" or user_choice == "Q":
            pass
