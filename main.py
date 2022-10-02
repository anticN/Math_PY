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
    print(f"Welcome to the Math-application written by Nikola Antic")
    print("=================================================================")
    time.sleep(1)
    print(f"What do you want to do with the programm?")
    user_choice = input(f"linear functions \033[1;32m(l/L)\033[0m, quadratic functions \033[1;32m(q/Q)\033[0m....")

    if user_choice == "l" or user_choice == "L":
        lin_func = LinearFunction()
        print()
        print("What do you want to do with the function?")
        print("===================================================================")
        lin_choice = input(f"Get the y-value with a x value\033[1;32m(y/Y)\033[0m. Get the x-value when y = 0 \033[1;32m(n/N)\033[0m. "
                           f"Add another function and get the point of intersection \033[1;32m(a/A)\033[0m")
        if lin_choice == "y" or lin_choice == "Y":
            lin_func.get_y_with_x(float(input(f"Type your x-value to get the y-value:")))
        elif lin_choice == "n" or lin_choice == "N":
            lin_func.get_x_when_y_0()
        elif lin_choice == "a" or lin_choice == "A":
            lin_func2 = LinearFunction()
            pass
    elif user_choice == "q" or user_choice == "Q":
        pass

