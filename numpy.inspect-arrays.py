#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

my_array= np.array([[1,2,3,4],
          [5,6,7,8]], dtype=np.int64)

print(my_array)

# Print the number of `my_array`'s dimensions
print(my_array.ndim)

# Print the number of `my_array`'s elements
print(my_array.size)

# Print information about `my_array`'s memory layout
print(my_array.flags)
print()
# Print the length of one array element in bytes
print(my_array.itemsize)
print()
# Print the total consumed bytes by `my_array`'s elements
print(my_array.nbytes)