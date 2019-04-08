#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 4/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

from functools import reduce
""" multiply all numbers in a list"""

data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x,y: x*y
print ( reduce(multiplier, data) )


product = 1
for x in data:
    product = product * x
    print(x)
print(product)