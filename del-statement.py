#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 29/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

numbers = list(range(0,10))
print (numbers)
del (numbers[-1])
print (numbers)

del(numbers[0:2]) #del from 0 to 2 no incluiding the 2
print (numbers)

del numbers[::3]
print (numbers)

#Deleting a Slice Representing the Entire List
del numbers[:]
print(numbers)

#Deleting a Variable from the Current Session
del numbers
print (numbers)