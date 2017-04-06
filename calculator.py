"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def evaluate_input(operand, parameter_1, parameter_2 = 0):

    """ 
    Step 1 of REPL
    This takes in the parameters and does the operand
    """

    if operand == "+":
        return add(parameter_1, parameter_2)

    elif operand == "-":
        return subtract(parameter_1, parameter_2)

    elif operand == "*":
        return multiply(parameter_1, parameter_2)

    elif operand == "/":
        return divide(parameter_1, parameter_2)

    elif operand == "square":
        return square(parameter_1)

    elif operand == "cube":
        return cube(parameter_1)

    elif operand == "pow":
        return power(parameter_1, parameter_2)

    elif operand == "mod":
        return mod(parameter_1, parameter_2)

# The While Loop runs the Calculator until told to Exit

while True:
    calculator_input = raw_input(">>>")
    
    # Here we tokenize the input 
    
    calculator_token = calculator_input.split(" ")

    # Check for exit variable

    if calculator_token[0] == "q":
        quit()

    else:
        if len(calculator_token) == 3:
            output = evaluate_input(calculator_token[0], int(calculator_token[1]), int(calculator_token[2]))
        else:
            output = evaluate_input(calculator_token[0], int(calculator_token[1]))
        
        print output
