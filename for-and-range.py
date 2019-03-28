#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
"""
Lists are enclosed in brackets:

l = [1, 2, "a"]

Tuples are enclosed in parentheses:

t = (1, 2, "a")

Tuples are faster and consume less memory. See Tuples for more information.

Dictionaries are built with curly brackets:

d = {"a":1, "b":2}

Sets are made using the set() builtin function. More about the data structures here below:
"""

list1 = [10, 20, 30]
list2 = [40, 50]
concatenated_list = list1 + list2

for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')


time_tuple = (9,16,1)
print(time_tuple[0] * 3600 + time_tuple[1]* 60 + time_tuple[2])

numbers = [1,2,3,4,5]

numbers +=(6,7)
print (numbers)
