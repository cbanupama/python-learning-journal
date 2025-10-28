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

