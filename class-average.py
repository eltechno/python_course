#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 20/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
""" Class average program with sequence controlled iteration"""

total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for number in grades:
    total += number
    grade_counter += 1
average = total / grade_counter
print(f"the class averge is: {average} ")