#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 3/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import math
def area(r):
    """ Area of a circle with radius R"""
    return math.pi * (r**2)

radii=[2,5,7.1,0.3,10]

#method1
areas = []
for i in radii:
    a= area(i)
    areas.append(a)
print(areas)

#method2
print(list(map(area, radii)))


