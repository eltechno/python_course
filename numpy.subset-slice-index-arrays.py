#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

my_array = np.array([1,2,3,4])
my_2d_array =  np.array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
my_3d_array = np.array([  [[ 1,  2,  3,  4],
                          [  5,  6,  7,  8]],
                          [[ 1,  2,  3,  4],
                          [  9, 10, 11, 12]]])


# Select the element at the 1st index
print(my_array[1])

# Select the element at row 1 column 2
print(my_2d_array[1][2])

# Select the element at row 1, column 2 and
for i in range(4):
    print(my_3d_array[1,1,i])

#y = np.ones([4,4])
#print(y)