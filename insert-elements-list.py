#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

color_names = ['orange', 'yellow', 'green']
#Inserting an Element at a Specific List Index
color_names.insert(0,'red')
print(color_names)

#Adding an Element to the End of a List
color_names.append('blue')
print(color_names)

#Adding All the Elements of a Sequence to the End of a List
color_names.extend(['indigo', 'violet'])
print(color_names)

sample_list = []
s='abc'

sample_list.extend(s)
print(sample_list)

t=(1,2,3)
sample_list.extend(t)
print(sample_list)

#Rather than creating a temporary variable, like t, to store a tuple before
# appending it to a list, you might want to pass a tuple directly to extend.
# In this case, the tuple’s parentheses are required, because extend expects
# one iterable argument:
sample_list.extend((4,5,6))
print(sample_list)

#Removing the First Occurrence of an Element in a List

color_names.remove('green')
print(color_names)

#Emptying a List
color_names.clear()
print(color_names)

#Reversing a List’s Elements

color_names = ['red', 'orange', 'yellow', 'green', 'blue']
print("normal list", color_names)
color_names.reverse()
print('lista en reverse', color_names)

#Copying a List
copied_list=color_names.copy()
print(copied_list)

#this is the same as copy
copied_list = color_names [:]