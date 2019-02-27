#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:26:20 2019

@author: techno
"""


menu = input("+ Add, - Substract, * Multiply, / Divide")
a = int(input("First number: ")) #
b = int(input("Second Number: "))

if (menu == "+"):
    print ("Adding..", a + b)
elif (menu == "-"):
    print ("Substracting..", a - b)
elif (menu == "*"):
    print ("Multiplying..", a * b)
elif (menu == "/"):
    if (b == 0):
        print ("divition by zero is not possible")
    else:
        print ("Multiplying..", a / b)
else:
    print("WRONG OPTION")