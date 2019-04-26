#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

months = {'January': 1, 'February': 2, 'March': 3}
months2 = {number: name for name, number in months.items()}
print(months2)

"""
Curly braces delimit a dictionary comprehension, and the expression to 
the left of the for clause specifies a key–value pair of the form key: 
value. The comprehension iterates through months.items(), unpacking 
each key–value pair tuple into the variables name and number. The 
expression number: name reverses the key and value, so the 
new dictionary maps the month numbers to the month names.

What if months contained duplicate values? As these become the keys in 
months2, attempting to insert a duplicate key simply 
updates the existing key’s value. So if 'February' and 'March' 
both mapped to 2 originally, the preceding code would have produced
"""

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
grades2 = {k: sum(v) / len(v) for   k, v in grades.items()}
print(grades2)

"""
The comprehension unpacks each tuple returned by grades.items() 
into k (the name) and v (the list of grades). Then, the 
comprehension creates a new key–value pair with the key 
k and the value of sum(v) / len(v), which averages the
 list’s elements.
"""



