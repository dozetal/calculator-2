"""A prefix-notation calculator.

Using the arithmetic-2.py file, adding list to the function variables in 
Calculator Part 1. 
"""

from arithmetic_2 import *


def evaluate_input(operand, nums):

    """ 
    Step 1 of REPL
    This takes in the parameters and does the operand
    """

    if operand == "+":
        return add(nums)

    elif operand == "-":
        return subtract(nums)

    elif operand == "*":
        return multiply(nums)

    elif operand == "/":
        return divide(nums)

    # elif operand == "square":
    #     return square(parameter_1)

    # elif operand == "cube":
    #     return cube(parameter_1)

    # elif operand == "pow":
    #     return power(parameter_1, parameter_2)

    # elif operand == "mod":
    #     return mod(parameter_1, parameter_2)

# The While Loop runs the Calculator until told to Exit

while True:
    calculator_input = raw_input(">>>")
    
    # Here we tokenize the input 
    
    calculator_token = calculator_input.split(" ")

# Here we define the operand as the first item in the list calculator_token
# With the numbers as the contents of the list, starting at second item in 
# list calculator_toke

    operand = calculator_token[0]
    nums = calculator_token[1:]

    # Check for exit variable

    if operand == "q":
        quit()

    else:
        output = evaluate_input(operand, nums)
        # if len(calculator_token) == 3:
        #     output = evaluate_input(calculator_token[0], int(calculator_token[1]), int(calculator_token[2]))
        # else:
        #     output = evaluate_input(calculator_token[0], int(calculator_token[1]))
        
        print output
