#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 9/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5,   4.0, 3.75]

for name, gpa in zip (names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')

a = [[77, 68, 86, 73],  # first student's grades
      [96, 87, 89, 81],  # second student's grades
      [70, 90, 86, 81]]  # third student's grades

for row in a:
    for item in row:
        print(item, end=' ')
    print()

