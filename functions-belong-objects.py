#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

s= 'hello'

print (s.lower())
print(s.upper())
print(s.__len__())
print(s.capitalize())
print(s.casefold())
print(s.expandtabs(4))

#how to import modules and use abbreviations
import statistics as stats

grades = [ 85, 93, 45, 87, 93]

print (stats.mean(grades))

def cube(number):
    print('id(number):' , id(number))
    return number **3

print (cube(3))

"""=============================================================================="""
x= 3 = global variable

def cube2(number):
    print('Number is x:', number is x) #x is a global variable
    return number ** 3

cube2(x)