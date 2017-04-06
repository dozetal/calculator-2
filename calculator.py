"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

# do_setup()
# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print output

# The While Loop runs the Calculator until told to Exit

while True:
    calculator_input = raw_input(">>>")
    calculator_token = calculator_input.split(" ")

# Here we tokenize the input 

    if calculator_token[0] == "q":
        quit

    elif:
        output = evaluate_input()
        print output


def evaluate_input(operand, parameter_1, parameter_2 = " "):

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

    