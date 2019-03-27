#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
""" Rolling a six-sided die 6k times"""

import random
frec1 = 0
frec2 = 0
frec3 = 0
frec4 = 0
frec5 = 0
frec6 = 0

for roll in range(6_000_000): #note underscore separators*
    face = random.randrange(1, 7)

    #increment appropiate face counter
    if face == 1:
        frec1 +=1
    elif face == 2:
        frec2 +=1
    elif face == 3:
        frec3 +=1
    elif face == 4:
        frec4 +=1
    elif face == 5:
        frec5 +=1
    elif face == 6:
        frec6 +=1

print(f'Face{"Frecuency":>13}')
print(f'{1:>4}{frec1:>13}')
print(f'{2:>4}{frec2:>13}')
print(f'{3:>4}{frec3:>13}')
print(f'{4:>4}{frec4:>13}')
print(f'{5:>4}{frec5:>13}')
print(f'{6:>4}{frec6:>13}')

"""
* The expression range(6,000,000) would be incorrect. 
Commas separate arguments in function calls, so 
Python would treat range(6,000,000) as a call to 
range with the three arguments 6, 0 and 0.
"""

