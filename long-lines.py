#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 15/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import math
example_value1 = (63/25) * (17+16*math.sqrt(5)) / (7+15*math.sqrt(5))
example_value2 = (63/25) * (17+16*math.sqrt(5)) / (7+15*math.sqrt(5))
print (example_value1 == example_value2)

example_value3 = (63/25) * (
                (17+16*math.sqrt(5))
                /
                (7+15*math.sqrt(5))
)

print (example_value3 == example_value1)