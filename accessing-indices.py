#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

colors = ['red', 'orange','yellow']
print(list(enumerate(colors)))

print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index}: {value}')

numbers = [10,100,1000,3000,4000,5000]

key=1000
if key in numbers:
    print(f'found {key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')
