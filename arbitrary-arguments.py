#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

"""
Functions with arbitrary argument lists, such as built-in functions min and max,
can receive any number of arguments. Consider the following min call:

        min(88, 75, 96, 55, 83)

The function’s documentation states that min has two required parameters
(named arg1 and arg2) and an optional third parameter of the form *args,
indicating that the function can receive any number of additional
arguments. The * before the parameter name tells Python to pack any
remaining arguments into a tuple that’s passed to the args parameter.
In the call above, parameter arg1 receives 88,
parameter arg2 receives 75 and parameter args receives the tuple (96, 55, 83).
"""

def average(*args):
    print(args) #print the list of elements
    print(len(args)) # print the amount of elements
    return sum(args) / len(args)

print(average(5,8,76,5,5,4,3,2))

grades = [88, 75, 96, 55, 83]
print(average(*grades)
