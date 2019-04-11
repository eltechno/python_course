#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 9/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

a = [[77, 68, 86, 73],  # first student's grades
      [96, 87, 89, 81],  # second student's grades
      [70, 90, 86, 81]]  # third student's grades

for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
lista= [enumerate(a)]
#print the type
print("return type: ", type(lista))
#print the content
print(list(enumerate(a)))