#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np

x = np.array([[ 1.,  1.,  1.,  1.],
              [ 1.,  1.,  1.,  1.],
              [ 1.,  1.,  1.,  1.]])

# Print the shape of `x`
print(x.shape)

# Resize `x` to ((6,4))
np.resize(x, (6,4))
x.resize((6,4))
print(x.shape)
print(x)