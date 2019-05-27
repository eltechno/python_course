#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np
x = np.ones((3,4))
print(x)

y = np.random.random((5,1,4))
print(y)
print()

print (x + y)
"""
You see that, even though x and y seem to have somewhat different dimensions, 
the two can be added together.

That is because they are compatible in all dimensions:

    Array x has dimensions 3 X 4,
    Array y has dimensions 5 X 1 X 4

"""