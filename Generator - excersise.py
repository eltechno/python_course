#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:41:52 2019

@author: techno
"""

"""
0 -500
** 2
then sum
"""

numberGenerator = (items ** 2
                   for items in range (501)
                   )


print (sum(numberGenerator))