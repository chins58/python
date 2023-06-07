# Import the math module
import math

# Define the add function
def add(a, b):
    return a + b

# Define the subtract function
def subtract(a, b):
    return a - b

# Define the multiply function
def multiply(a, b):
    return a * b

# Define the divide function
def divide(a, b):
    return a / b

# Define the square root function
def square_root(a):
    return math.sqrt(a)

# Define the power function
def power(a, b):
    return math.pow(a, b)

# Define the factorial function
def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

# Start the main loop
while True:
    # Get the first number from the user
    number_1 = float(input("Enter the first number: "))

    # Get the operator from the user
    operator = input("Enter the operator (+, -, *, /, sqrt, power, factorial): ")

    # Get the second number from the user
    number_2 = float(input("Enter the second number: "))

    # Perform the calculation
    if operator == "+":
        result = add(number_1, number_2)
    elif operator == "-":
        result = subtract(number_1, number_2)
    elif operator == "*":
        result = multiply(number_1, number_2)
    elif operator == "/":
        result = divide(number_1, number_2)
    elif operator == "sqrt":
        result = square_root(number_1)
    elif operator == "power":
        result = power(number_1, number_2)
    elif operator == "factorial":
        result = factorial(number_1)
    else:
        print("Invalid operator!")
        continue

    # Display the result
    print("The result is", result)

    # Check if the user wants to continue
    continue_calculation = input("Do you want to continue? (y/n): ")
    if continue_calculation == "n":
        break
