'''
You can check the version of Python by importing the sys module.
We will need to import many modules throughout our coding journey.
Importing a module gives you access to more functionality!
Python runs code from the top of the file to the bottom
That is why imports (like sys) are usually placed at the top
'''

import sys

# Clear the terminal (works on many systems)
print("\033c")

'''
The "Hello, World!" program is the first program for many developers.
By creating this program, you are now officially a programmer!
Allow me to be the first to welcome you to the multiverse of programming!

In Python, you will write Python (.py) files
These files will be executed in the python interpreter
I created a Hello World.py file right here in Visual Studio Code
You are welcome to use any Integrated Development Environment (IDE)

This program only has one line of code and the output should be hello, world
It's as simple as that!
'''

print ("hello, YouTube!\n")

'''
Let's use the sys module to check the version of Python that we are using
Modules that I import will be at the very beginning of my programs 
We will learn more about many more modules as we go along!
'''

print(sys.version + "\n\n\n")

# Extra note: \n is a special character called an "escape sequence"
# It makes the text jump to a new line. \t would add a tab space.