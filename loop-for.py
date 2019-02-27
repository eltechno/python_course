#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:46:02 2019

@author: techno
"""
result = 0

for i in  range(4):
    number = int(input("Please give me the number: "))
    result += number
    
print ("the result of adding numbers is: ", result)


# =============================================================================
# imprime los numeros divisibles en 2
# =============================================================================
for i in range (1000):
    if (i%2 == 0):  
        print(i," is even number")
