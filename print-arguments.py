#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 19/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

for character in 'Programing':
    print(character, end='  ') #the end parameter

"""
Function print’s end Keyword Argument

The built-in function print displays its argument(s), then moves the cursor to the next line. 
You can change this behavior with the argument end, as in

print(character, end='  ')

which displays character’s value followed by two spaces. So, all the characters display 
horizontally on the same line. Python calls end a keyword argument, but end itself is not 
a Python keyword. Keyword arguments are sometimes called named arguments. 
The end keyword argument is optional. If you do not include it, print uses a newline 
('\n') by default. The Style Guide for Python Code recommends placing no spaces around 
a keyword argument’s =.
"""

for character2 in 'Programing':
    print(character2, sep=', ') # argument sep

print(10,20,30, sep=', ') #argument sep
"""
Function print’s sep Keyword Argument

You can use the keyword argument sep (short for separator) to specify the string that 
appears between the items that print displays. When you do not specify this argument, 
print uses a space character by default. Let’s display three numbers, each separated 
from the next by a comma and a space, rather than just a space:

Click here to view code image

In [2]: print(10, 20, 30, sep=', ')
10, 20, 30

To remove the default spaces, use sep='' (that is, an empty string).
"""