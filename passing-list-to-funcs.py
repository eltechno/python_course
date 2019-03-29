#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 29/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

def modify_list(items):
    """multiplies all elemtents of a list by 2"""
    for i in range(len(items)):
        items[i] *=2

numbers = [10,3,7,1,9]
modify_list(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


