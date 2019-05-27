#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np

a = np.array([ True,True,False,False])
b = np.array([ True,False,True,False])

print ( np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.logical_not(a,b))

"""
However, you can also compare entire arrays with each other! In this case,
 you use the np.array_equal() function. Just pass in the two arrays that 
 you want to compare with each other, and you’re done.

Note that, besides comparing, you can also perform logical operations 
on your arrays. You can start with np.logical_or(), np.logical_not() 
and np.logical_and(). This basically works like your typical OR, 
NOT and AND logical operations;

In the simplest example, you use OR to see whether your elements are the same 
(for example, 1), or if one of the two array elements is 1. If both of them 
are 0, you’ll return FALSE. You would use AND to see whether your second 
element is also 1 and NOT to see if the second element differs from 1.
"""