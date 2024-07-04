'''
PROJECT 1: Build a Multi-Function Calculator
[...]
For this challenge, you need to create a multi-function calculator using Python that takes input and does the following:
•	solve proportions
•	solve for x in equations
•	factor square roots
•	convert decimals to fractions and percents
•	convert fractions to decimals and percents
•	convert percents to decimals and fractions
[...]
'''

import math
import sympy
from sympy import symbols
from sympy.solvers import solve


###############################################
# CALCULATOR FUNCTIONS

def add():
    a = input("Enter a first summand: ")
    b = input("Enter a second summand: ")
    if is_number(a) and is_number(b):
        result = float(a) + float(b)
        if result == int(result):
            result = int(result)
        print(f"The sum of your numbers is {result}.")
    else:
        for val in (a, b):
            if not is_number(val):
                print(f"ERROR: {val} is not a valid number!")

def subtract():
    a = input("Enter a minuend: ")
    b = input("Enter a subtrahend: ")
    if is_number(a) and is_number(b):
        result = float(a) - float(b)
        if result == int(result):
            result = int(result)
        print(f"The difference of your numbers is {result}.")
    else:
        for val in (a, b):
            if not is_number(val):
                print(f"ERROR: {val} is not a valid number!")

def multiply():
    a = input("Enter a first factor: ")
    b = input("Enter a second factor: ")
    if is_number(a) and is_number(b):
        result = float(a) * float(b)
        if result == int(result):
            result = int(result)
        print(f"The product of your numbers is {result}.")
    else:
        for val in (a, b):
            if not is_number(val):
                print(f"ERROR: {val} is not a valid number!")

def divide():
    a = input("Enter a dividend: ")
    b = input("Enter a divisor: ")
    if is_number(a) and is_number(b):
        result = float(a) / float(b)
        if result == int(result):
            result = int(result)
        print(f"The quotient of your numbers is {result}.")
    else:
        for val in (a, b):
            if not is_number(val):
                print(f"ERROR: {val} is not a valid number!")

def prime_factors():
    a = input("Enter a whole number: ")
    try:
        prime_factors = ", ".join(map(str, get_prime_factors(int(a))))
        print(f"The prime factors of {a} are: {prime_factors}.")
    except ValueError:
        print(f"ERROR: {a} is not a valid number!")

def simplify_sqrt():
    a = input("Without the radical, enter a square root to factor: ")
    try:
        a = int(a)
        upper_limit = math.floor(math.sqrt(a)) + 1
        max_factor = 1
        other_factor = 1
        square_root = 1
        for nr in range(1, upper_limit):
            if a % (nr**2) == 0:
                max_factor = nr**2
        other_factor = a/max_factor
        
        square_root = int(math.sqrt(max_factor))
        other_factor = int(other_factor)
        print(f"The simplified square root of your number is {square_root * sympy.sqrt(other_factor)}.")
    except ValueError:
        print(f"ERROR: {a} is not a valid input!")

def solve_for_x():
    x = symbols("x")
    eq = input("Enter an equation to solve for x: 0 = ")
    res = solve(eq, x)
    print("x = ", res)

def get_binary_representation():
    a = input("Enter a whole number: ")
    try:
        print(f"The binary representation of your number is {int(a):08b}.")
    except ValueError:
        print(f"ERROR: {a} is not a valid number!")


###############################################
# HELPER FUNCTIONS

def get_prime_factors(val):
    i = 2
    factors = []
    while i * i <= val:
        if val % i:
            i += 1
        else:
            val //= i
            factors.append(i)
    if val > 1:
        factors.append(val)
    return factors

def is_number(val):
    try:
        float(val)
        return True
    except ValueError: 
        return False


###############################################
# USER MENU WITH PROMPTS FOR INTERACTING WITH THE USER

print("*** WELCOME TO THIS LITTLE CALCULATOR PROGRAM ***")
print("You can select one of the following options in order to carry out the specified mathematical operation: ")
print("  1. Add two numbers\n  2. Subtract two numbers\n  3. Multiply two numbers\n  4. Divide two numbers")
print("  5. Get the prime factors of a (whole) number\n  6. Simplify the square root of a number\n  7. Solve for variable")
print("  8. Get the binary representation of a (whole) number")

user_option = input("Please choose one of these options: ")
match user_option:
    case "1":
        add()
    case "2":
        subtract()
    case "3":
        multiply()
    case "4":
        divide()
    case "5":
        prime_factors()
    case "6":
        simplify_sqrt()
    case "7":
        solve_for_x()
    case "8":
        get_binary_representation()
    case _:
        print("--> You did not select any of the specified options!")

