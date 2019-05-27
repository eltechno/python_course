#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

my_array2= np.genfromtxt('data2.txt',
                         skip_header=1,
                         filling_values=-999)
print(my_array2)

"""
You see that here, you resort to genfromtxt() to load the 
data. In this case, you have to handle some missing values 
that are indicated by the 'MISSING' strings. Since the 
genfromtxt() function converts character strings in numeric 
columns to nan, you can convert these values to other ones 
by specifying the filling_values argument. In this case, 
you choose to set the value of these missing values to -999.
"""