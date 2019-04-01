#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

#Counting the Number of Occurrences of an Item List method count searches
# for its argument and returns the number of times it is found:

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1,6): #NUMEROS DEL 1 AL 5
    print(f'{i} appears {responses.count(i)} times in responses')



