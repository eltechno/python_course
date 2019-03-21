#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 21/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

"""
compound interest
a = p(1+ r )^n

p is the original amount invested (i.e the principal)
r is the annual interest rate
n is the number of years and
a is the amount on deposit at the end of the nth year
"""
principal = 100
rate = 0.4
for year in range(1,10):
    amount =  principal * ((1+ rate) ** year)
    print(f'{year:>2}{amount:>10.2f}')


