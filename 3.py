# 1. Write a Python program that asks the user for their name and age, 
# then prints a personalized greeting message. 
# Use both the + operator and f-strings for output.

name = input("Enter your name: ")
age = input("Enter your age: ")
# Using + operator
print("Hello, " + name + "! You are " + age + " years old.")
# Using f-strings
print(f"Hello, {name}! You are {age} years old.")

# Write a Python program that:

# Takes a sentence as input from the user.
# Prints the sentence in all uppercase and lowercase.
# Replaces all spaces with underscores.
# Removes leading and trailing whitespace.

sentence = input("Enter a sentence: ")
# Print in uppercase
print("Uppercase:", sentence.upper())
# Print in lowercase
print("Lowercase:", sentence.lower())
# Replace spaces with underscores
print("With underscores:", sentence.replace(" ", "_"))
# Remove leading and trailing whitespace
print("Trimmed sentence:", sentence.strip())

# Write a Python program that:

# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.

user_string = input("Enter a string: ")
# Count characters excluding spaces
char_count = len(user_string.replace(" ", ""))
print("Number of characters (excluding spaces):", char_count)   

# Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:

# Example:

# Hello
#     World
# This is a backslash: \
print("Hello\n\tWorld\nThis is a backslash: \\")