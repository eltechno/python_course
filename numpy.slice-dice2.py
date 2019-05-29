#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 29/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np
np_2d= np.array([[1.73,1.68,1.71,1.89,1.79],
                 [65.4,59.2,63.6,88.4,68.7]])

print(np_2d.shape)

#second row, index 3
print(np_2d[1][3], end="\n\n")

# second row index 0
print(np_2d[1,0], end="\n\n")

#both rows index 1 to 3 with including value of the 3
print(np_2d[:,1:3], end="\n\n")

#all the second row
print(np_2d[1,:], end="\n\n")
