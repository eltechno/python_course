#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 19/03/19

#Feature:  # check what is the minimun number among 3 numbers
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

number1 = int(input("Enter the 1 number"))
number2 = int(input("Enter the 2 number"))
number3 = int(input("Enter the 3 number"))

minimum = number1
if number2 < minimum:
    minimum = number2
if number3 < minimum:
    minimum= number3
print("the smallest number is :", minimum)
