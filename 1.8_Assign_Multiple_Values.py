print("\033c")

'''
Python allows you to assign values to multiple variables in one line:
Note: Make sure the number of variables matches the number of values, or else you will get an error.
'''

x, y, z = "Jasper", "Lyla", "Finn"
print(x)
print(y)
print(z)

print("\n")

# And you can assign the same value to multiple variables in one line:

a = b = c = "Theo"
print(a)
print(b)
print(c)

print("\n")

'''
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. 
This is called unpacking.
'''

fruits = ["apple", "banana", "cherry"]
one, two, three = fruits
print(one)
print(two)
print(three)