#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 21/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
"""
Here we continue our discussion of using statistics to analyze data with several additional descriptive
statistics, including:

    mean—the average value in a set of values.

    median—the middle value when all the values are arranged in sorted order.

    mode—the most frequently occurring value.

These are measures of central tendency—each is a way of producing a single value that represents a
“central” value in a set of values, i.e., a value which is in some sense typical of the others
"""

import decimal
import statistics

grades = [85, 93, 45, 89, 85]
media = sum(grades) / len(grades)
print (media)


statistics.mean(grades)