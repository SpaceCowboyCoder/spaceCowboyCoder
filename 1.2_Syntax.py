print("\033c")

'''
Syntax in programming refers to the set of rules that define the structure and 
format of a programming language, determining how symbols, punctuation, and
words can be combined to create valid statements. Without proper syntax, code
cannot be correctly interpreted or executed by a computer.

You will see syntax errors. Get used to it.

Indentation refers to the spaces at the beginning of a line of code
Some programming languages only use indentation to help with readability
In Python, we will use indentation to indicate blocks of code that go together
'''

x = input("\nEnter your age: ")

if x.isdigit():
    age = int(x)
    if age < 16:
        print("You are not old enough to drive.\n")
    else:
        print("You are old enough to drive.\n")
else:
    print("Invalid entry, try again.\n")

'''
Let's see what happens if you forget the indentation:

x = input("Enter your age: ")

if x.isdigit():
age = int(x)
if age < 16:
print("You are not old enough to drive.\n")
else:
print("You are old enough to drive.\n")
else:
print("Invalid entry, try again.\n")
'''