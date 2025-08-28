print("\033c")

'''
Adding comments to your code is EXTREMELY important when programming
A single-line comment starts with a #
The rest of the line will be ignored by the interpreter
Usually single-line comments are above a block of code, or 
They are often used on the same line as a line of code


# Comments (like this one) are ignored by Python
# They're notes for humans, not the computer
# We will use them throughout our programs to explain what’s going on

# Python is case sensitive!
# print("hello") works, but Print("hello") or PRINT("hello") would cause an error

# Our very first line of code:
'''

# This is a single-line comment

print("hello, world\n") # Prints "hello, world" in the console/terminal

'''
Technically, Python does not have an official syntax for mult-line comments
However, surrounding lines of code in triple quotations has this effect
I use multi-line comments for these messages that I write

IMPORTANT
Comments are a VERY POWERFUL tool that you can use for debugging
Have a line of code that is giving you problems? Comment it out!
'''

x = input("Enter your age: ") # Declaring variable used for input

if x.isdigit(): # Checks to see if data entered is a digit
age = int(x)

# Checking how user's age compares to 16
if age < 16:
print("You are not old enough to drive.\n")
else:
print("You are old enough to drive.\n")
else: # For anything else entered (garbage)
print("Invalid entry, try again.\n") 
