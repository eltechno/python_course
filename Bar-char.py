#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

"""display a bar chart"""

numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart for numbers: ')
print (f'Index{"value" :>8} Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

