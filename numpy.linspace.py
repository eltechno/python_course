#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

#Creating Floating-Point Ranges with linspace
#You can produce evenly spaced floating-point ranges with
# NumPy’s linspace function. The function’s first two
# arguments specify the starting and ending values in the range,
# and the ending value is included in the array. The optional
# keyword argument num specifies the number of evenly spaced
# values to produce—this argument’s default value is 50:
import numpy as np
floats_array = np.linspace(0.0, 1.0, num=5)
print(floats_array)