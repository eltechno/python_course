#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:21:56 2019

@author: techno
"""

"""
There are four collection data types in the Python programming language:

List    []       is a collection which is ordered and changeable. Allows duplicate members.
Tuple   ()       is a collection which is ordered and unchangeable. Allows duplicate members.
Set     {}       is a collection which is unordered and unindexed. No duplicate members.
Dictionary   {}  is a collection which is unordered, changeable and indexed. No duplicate members.



"""
names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celsius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

nameLength =  {
        name : len(name) #colocar la longitud de los nombres
        for name in names
        #if name.startswith("A")    #names that start with A only
        }

numbersMulti = {
        items: (items * items)
        for items in range (1,500) # we can add range(1,500)
        #for items in numbers # we can add range(1,500)
        # if number > 30
        # if number < 120
}

fahrenheit = {
        key: celsius * (9/5 ) + 32
        for key, celsius in celsius.items()
        if celsius > -10
        if celsius < 20
}
print (fahrenheit)