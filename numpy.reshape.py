#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np

# 3 x 4 array
x = np.array([[ 1.,  1.,  1.,  1.],
              [ 1.,  1.,  1.,  1.],
              [ 1.,  1.,  1.,  1.]])

# Print the size of `x` to see what's possible
print(x)
print(x.size)

# Reshape `x` to (2,6)
print(x.reshape((2,6)), end="\n\n")


# Flatten `x`
z = x.ravel()

# Print `z`
print(z)