#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 9/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import math

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
reversed_numers= [item ** 2 for item in reversed(numbers)]
print(reversed_numers )

range_of_numbers = [numeros **2 for numeros in range(1,100)]
print (range_of_numbers)

remainders5 = [x**2 % 5 for x in range (1,101)]
print(remainders5)

test  = (10 ** 2 % math.pi)
numero_pi = round(float (math.pi), 3)
print(numero_pi)

A = [1,3,5,7]
B = [2,4,6,8]
C = ["g","f","d","s"]

cartesian_product= [(a,b,c) for a in A for b in B for c in C]
print(cartesian_product)

