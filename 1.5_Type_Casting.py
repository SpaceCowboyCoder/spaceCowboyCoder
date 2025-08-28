print("\033c")

'''
Remember, a Variable is declared (created) as soon as you assign a value to it
You could think of a variable as a containers that store different types of data
We can use type casting to "change" or specify the type of data stored in a variable
'''

print("\n")

age = 0 # This variable is storing a value of type int (an integer)
myString = "hello, world" # This variable is storing a value of type str (a String is a sequence of characters surrounded in " ")
year = 2025
birthYear = input("What year were you born? ") # When using the input function, the DEFAULT data type is str
hadBirthday = True

if birthYear.isdigit():
    birthYear = int(birthYear) # Type casting birthYear; int required for calculations
else:
    print("Invalid entry, try again.\n")
    exit()

if hadBirthday == True:
    age = year - birthYear
    print("You are " + str(age) + " years old!\n") # type casting age; print function requires Strings
elif hadBirthday == False:
    age = year - birthYear - 1
    print("You are " + str(age) + " years old!\n")


# Note: You can have Python tell you the type of data stored in a variable using the type function
x = 5
y = "John"
print(type(x))
print(type(y))

print("\n")




