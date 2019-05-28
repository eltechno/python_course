#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np

my_2d_array =  np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8]])

print(my_2d_array)
print(np.transpose(my_2d_array))

print()
# making a 3x3 array
gfg = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# before transpose
print(gfg, end='\n\n')
#, end='\n\n' add two blank spaces

# after transpose
print(gfg.transpose())

print()

# Create 3 x 3 matrix
mat = np.array([[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3]])

print(mat)
print(mat.T)

#Transposing numpy array with 3 dimensions (tensors)
tensor = np.array([[ [1, 2], [3, 4] ],
                   [ [5, 6], [7, 8] ]])
print(tensor.shape)
print(tensor.T)