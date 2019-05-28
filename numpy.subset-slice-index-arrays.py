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

# Select items at index 0 and 1
print(my_array[0:2])

# Select items at row 0 and 1, column 1
print(my_2d_array[0:2,1])

# Select items at row 1
# This is the same as saying `my_3d_array[1,:,:]
print(my_3d_array[0,...])

"""
a[start:end] # items start through the end (but the end is not included!)
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through the end (but the end is not included!)
"""
print()
# Try out a simple example
print(my_array[my_array<2])

# Specify a condition
bigger_than_3 = (my_3d_array >= 3)

# Use the condition to index our 3d array
print(my_3d_array[bigger_than_3])


print(" first print")
# Select elements at (1,0), (0,1), (1,2) and (0,0)
print(my_2d_array[[1, 0, 1, 0],[0, 1, 2, 0]])
print("second print")
# Select a subset of the rows and columns
print(my_2d_array[[1, 0, 1, 0]][:,[0,1,2,0]])