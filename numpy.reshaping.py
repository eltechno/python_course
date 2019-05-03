#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

#Note the chained method calls in the preceding snippet. First, arange produces an array
# containing the values 1–20. Then we call reshape on that array to get the 4-by-5 array t
# hat was displayed.
#You can reshape any array, provided that the new shape has the same number of
# elements as the original. So a six-element one-dimensional array can become
# a 3-by-2 or 2-by-3 array, and vice versa, but attempting to reshape a
# 15-element array into a 4-by-4 array (16 elements) causes a ValueError
import numpy as np
array_one = np.arange(1,21)
print(array_one)
print ()

array_one = np.arange(1,21).reshape(4, 5)
print(array_one)

#Displaying Large arrays
#When displaying an array, if there are 1000 items or more, NumPy drops the middle rows
# , columns or both from the output. The following snippets generate 100,000 elements
# . The first case shows all four rows but only the first and last three of the 25,000
# columns. The notation ... represents the missing data. The second case shows t
# he first and last three of the 100 rows, and the first and last three of the
# 1000 columns:
import timeit
large_array =np.arange(1, 100001).reshape(4, 25000)

print(large_array)
