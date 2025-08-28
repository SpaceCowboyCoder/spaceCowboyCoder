print("\033c")

'''
The Python print() function is often used to output variables.
'''

x = "Python is awesome!"
print(x)

'''
In the print() function, you output multiple variables, separated by a comma:
'''

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

'''
You can also use the concatenation operator (+) to output multiple variables.
Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
'''

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

'''
For numbers, the + character works as a mathematical operator:
'''

x = 5
y = 10
print(x + y)

'''
In the print() function, when you try to combine a string and a number with 
the + operator, Python will give you an error:
'''

x = 5
y = "John"
print(x + y)

# Fix this with type casting

x = 5
y = "John"
print(str(x) + y)

'''
The best way to output multiple variables in the print() function is to separate 
them with commas, which even support different data types:
'''

x = 5
y = "John"
print(x, y)