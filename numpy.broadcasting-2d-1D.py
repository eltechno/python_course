#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 27/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import numpy as np

x = np.ones((3,4))
print(x.shape)
print(x)

y=np.arange(4)
print(y.shape)
print(y)

print(x-y)