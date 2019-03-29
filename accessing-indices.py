#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

colors = ['red', 'orange','yellow']
print(list(enumerate(colors)))

print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index}: {value}')
