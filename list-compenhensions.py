#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

list1=[]
for item in range(1,6):
    list1.append(item)
print(list1)

list2 = [item for item in range(1,6)]
print(list2)

list3 = list(range(1,6))
print(list3)

list4=[item **3 for item in range(1,5)]
print(list4)

list5=[item for item in range(1,11) if item %2 ==0]
print(list5)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors2= [item.upper() for item in colors]
print(colors2)
