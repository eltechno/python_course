#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:19:27 2019

@author: techno


There are four collection data types in the Python programming language:

List    []       is a collection which is ordered and changeable. Allows duplicate members.
Tuple   ()       is a collection which is ordered and unchangeable. Allows duplicate members.
Set     {}       is a collection which is unordered and unindexed. No duplicate members.
Dictionary   {}  is a collection which is unordered, changeable and indexed. No duplicate members.



"""

guestList = [
        ('Paulo', 41, 'man'),
        ('Cesar', 23, 'man'),
        ('Tita', 32, 'woman')
        ]

for name, age, sex in guestList:
    print ("Name: ", name)
    print ("Age: ", age)
    print ("Sex: ", sex)
    print ()