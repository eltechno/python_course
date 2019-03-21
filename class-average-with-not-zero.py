#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 20/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

total = 0
grade_counter = 0

grade = int(input('Enter grade, -1 to end: '))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))

if grade_counter != 0:
    average = total / grade_counter
    print(f"Class average is {average:.2f}")
else:
    print('No grades were entered')