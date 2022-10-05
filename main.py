import os
import time
from linearFunction import LinearFunction, WrongDatatypeException
from termcolor import colored
"""
@author Nikola Antic
@version 0.1
@since 2022-10-02
"""

# ! Please define functions at the top!
def get_point(func1, func2):
    xi = (lin_func.b - lin_func2.b) / (lin_func2.a - lin_func.a)
    yi = lin_func.a * xi + lin_func.b
    print(f"The intersection point of the two functions is: ({xi}|{yi})\n")

if __name__ == '__main__':
    print(f"Hello {os.getlogin()}")

    print(f"Welcome to the Math-application written by Nikola Antic")
    print("=================================================================")
    while True:
        print()
        print(f"What do you want to do with the programm?")
        print(f"""
        1. Create a linear function {colored('(l)', 'green')}
        2. Create a quadratic function {colored('(q)', 'green')}""")
        user_choice = input()

        if user_choice.lower() == "l":
            a = input("Enter a > ")
            b = input("Enter b >")
            try:
                lin_func = LinearFunction(a, b)
                lin_functions = []
                lin_functions.append(lin_func)
            except WrongDatatypeException as wrongData:
                print(wrongData)
            print()
            lin_func.print()
            #time.sleep(1)
            while True:
                print()
                print("What do you want to do with the function?")
                print("=================================================================")
                # For multiline strings use triple quotes and you'd rather print than using the input prompt
                print(f"""
                1. Get the y-value with an x-value {colored('(y)', 'green')}
                2. Get the x-value when y = 0 {colored('(x)', 'green')}
                3. Get the point of intersection with another function {colored('(i)', 'green')}
                4. Calculate with a new function {colored('(n)', 'green')}
                5. Exit {colored('(e)', 'green')}""")
                lin_choice = input()
                if lin_choice.lower() == "y":
                    lin_func.get_y_with_x(float(input(f"Type your x-value to get the y-value:")))
                elif lin_choice.lower() == "x":
                    lin_func.get_x_when_y_0()
                elif lin_choice.lower() == "i":
                    lin_func2 = LinearFunction(a, b)
                    get_point(lin_func, lin_func2)
                elif lin_choice.lower() == "n":
                    lin_func = LinearFunction()
                    lin_func.print()
                elif lin_choice.lower() == "e":
                    break
        elif user_choice.lower() == "q":
            pass
