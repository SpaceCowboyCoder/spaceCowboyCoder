print("\033c")

'''
Variables can have a short name (like x) or a more descriptive name (age, carMake, sum_mass).

RULES FOR NAMING VARIABLES:

1. Must start with a letter or the underscore character
2. Cannot start with a number
3. Can only contain alpha-numeric characters and underscores (A-z, 0-9, _ )
4. Variable names are case-sensitive (name and Name are different variables)
5. A variable name cannot be any of the Python keywords.
'''

print("\n")

# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names
2myvar = "John"
my-var = "John"
my var = "John"

print("\n")

'''
MULTI-WORD VARIABLE NAMES

CAMEL CASE
Each word, except the first, starts with a capital letter:
myVariableName = "John"

PASCAL CASE
Each word starts with a capital letter:
MyVariableName = "John"

SNAKE CASE
Each word is separated by an underscore character:
my_variable_name = "John"
'''