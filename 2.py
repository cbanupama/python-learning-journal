#1. Arithmetic Practice: 
# Write a Python program that performs basic arithmetic operations
# (addition, subtraction, multiplication, and division)on two numbers.
# Define the two numbers as variables within the code and 
# print the results for each operation.

# Define two numbers
num1 = 15
num2 = 3

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)    

# Swap Two Variables:
# Write a Python program that swaps the values of two variables
# with and without using a third variable.

# Define two variables
a = 5
b = 10
# Swap using a third variable
temp = a
a = b
b = temp
print("After swapping with a third variable: a =", a, ", b =", b)
# Reset values
a = 5
b = 10
# Swap without using a third variable
a, b = b, a
print("After swapping without a third variable: a =", a, ", b =", b)
