#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 29/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np
#generate random data to create info for testing

height = np.round(np.random.normal(1.75 , 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

#join information to create two columns array
np_city = np.column_stack((height,weight))
print(np_city)