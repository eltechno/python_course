#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import numpy as np

#import data
x, y , z = np.loadtxt('data.txt',
                      skiprows=1,
                      unpack=True)
print(x)
print(y)
print(z)

"""
In the code above, you use loadtxt() to load the data in your environment. 
You see that the first argument that both functions take is the text file 
data.txt. Next, there are some specific arguments for each: in the first
statement, you skip the first row, and you return the columns as separate 
arrays with unpack=TRUE. This means that the values in column 
Value1 will be put in x, and so on.
Note that, in case you have comma-delimited data or if you want 
to specify the data type, there are also the arguments 
delimiter and dtype that you can add to the loadtxt() arguments.
"""