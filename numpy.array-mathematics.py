#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

x = np.array([[1,2,3],
 [3,4,5]])
y = np.array([6,7,8])


# Add `x` and `y`
print (np.add(x,y) )

# Subtract `x` and `y`
np.subtract(x,y)

# Multiply `x` and `y`
np.multiply(x,y)

# Divide `x` and `y`
np.divide(x,y)

# Calculate the remainder of `x` and `y`
np.remainder(x,y)

"""
Remember how broadcasting works? Check out the dimensions and the shapes of 
both x and y in your IPython shell. Are the rules of broadcasting respected?

But there is more.

Check out this small list of aggregate functions:
a.sum() 	Array-wise sum
a.min() 	Array-wise minimum value
b.max(axis=0) 	Maximum value of an array row
b.cumsum(axis=1) 	Cumulative sum of the elements
a.mean() 	Mean
b.median() 	Median
a.corrcoef() 	Correlation coefficient
np.std(b) 	Standard deviation

Besides all of these functions, you might also find it useful to know that there are 
mechanisms that allow you to compare array elements. For example, if you want to 
check whether the elements of two arrays are the same, you might use the == operator. 
To check whether the array elements are smaller or bigger, you use the < or > operators.
"""