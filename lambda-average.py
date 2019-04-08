#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 4/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

""" create a program to check if the list of numbers is above of below the average"""

import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

""" print all the values major than media"""
print(list(filter(lambda x: x > avg, data)))

""" print all the values above than media"""
print(list(filter(lambda x: x < avg, data)))

#Remove  missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "Ecuador", "", "", "Venezuela" ]

print(list(filter(None,countries)))

#False Values
#"", 0, 0.0, 0j, [], (), {}, Flase, None, instances which signal they are empty

