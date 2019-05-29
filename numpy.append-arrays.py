#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

my_array = np.array([1, 2, 3, 4])
print(my_array)

# Append a 1D array to your `my_array`
new_array = np.append(my_array, [7, 8, 9, 10])
print(new_array, end="\n\n")

my_2d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])
print(my_2d_array, end="\n\n")

# Append an extra column to your `my_2d_array`
new_2d_array = np.append(my_2d_array, [[7], [8]], axis=1)
print(new_2d_array)

"""         
Note how, when you append an extra column to my_2d_array, 
the axis is specified. Remember that axis 1 indicates the 
columns, while axis 0 indicates the rows in 2-D arrays.
"""