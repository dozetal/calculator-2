# This is part 2 of calculator-2 in which all functions take lists as inputs

def add(num_list):
    """Return the sum of two numbers incl list"""
    sum = 0
    for item in num_list:
        sum = sum + int(item)
    return sum

# def add(num1, num2):
#     """Return the sum of two numbers"""
#     return num1 + num2

def subtract(num_list):
    """Return the difference of two numbers"""
    answer = 0
    for item in num_list:
        answer = answer - int(item)
    return answer    

def multiply(num_list):
    """Return the product of two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / float(num2)

def square(num):
    """Return the square of a number"""
    return num **2

def cube(num):
    """Return the cube of a number"""
    return num **3

def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num **exponent

def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2

def add_mult(num1, num2, num3):
    """
    This takes three numbers
    It adds the first two numbers and returns the sum
    Then it muliples the sum by the third number
    and returns that result 
    """
    
    sum1 = add(num1, num2)
    return sum1 * num3
