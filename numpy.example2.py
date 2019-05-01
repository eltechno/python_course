#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 30/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
#Enter steps here

import numpy as np
integers = np.array([[1,2,3],[4,5,6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

#Determining an array’s Element Type
#The array function determines an array’s element type
# from its argument’s elements. You can check the
# element type with an array’s dtype attribute:

print(integers.dtype)
print(floats.dtype)


#Determining an array’s Dimensions
#The attribute ndim contains an array’s number of dimensions and the attribute
# shape contains a tuple specifying an array’s dimensions:
print(integers.ndim)
print(floats.ndim)

#Here, integers has 2 rows and 3 columns (6 elements) and floats is one-dimensional,
# so snippet [11] shows a one-element tuple (indicated by the comma) containing floats’
# number of elements (5)
print(integers.shape)
print(floats.shape)

#Determining an array’s Number of Elements and Element Size
#You can view an array’s total number of elements with the
# \attribute size and the number of bytes required to store
# each element with itemsize:

print(integers.size)
print(integers.itemsize)
#Note that integers’ size is the product of the shape tuple’s
# values—two rows of three elements each for a total of six
# elements. In each case, itemsize is 8 because integers
# contains int64 values and floats contains float64 values,
# which each occupy 8 bytes.
print(floats.size)
print(floats.itemsize)

#iterating Through a Multidimensional array’s Elements

for row in integers:
    print(row)
    for column in row:
        print(column, end="     ")
    print()

#You can iterate through a multidimensional array as if it were
# one-dimensional by using its flat attribute:

for i in integers.flat:
    print(i, end="   ")
print()
# Filling arrays with Specific Values
#NumPy provides functions zeros, ones and full for creating
# arrays containing 0s, 1s or a specified value, respectively.
# By default, zeros and ones create arrays containing float64 values

array_uno = np.zeros(5)
print(array_uno)

#For a tuple of integers, these functions return a
# multidimensional array with the specified dimensions.
# You can specify the array’s element type with the
# zeros and ones function’s dtype keyword argument

array_dos = np.ones((2,4), dtype=int)
print(array_dos)

#The array returned by full contains elements with the second argument’s value and type:

array_tres = np.full((3,5), 13)
print(array_tres)
