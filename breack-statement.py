#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 21/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

""" how to use the break statement and continue """

for number in range(100):
    if number == 10:
        break
    print(number, end=" ")
print("")

for number in range(10):
    if number == 5:
        continue
    print(number, end=" ")