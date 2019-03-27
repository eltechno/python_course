#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import random # import the random module
random.seed(1)
""" generate random numbers from a rolling dice"""
for roll in range(10):
    print(random.randrange(1, 7), end=' ')
#randrange generate an integer from a 1st arg, up to (not including) the second arg
"""
Seeding the Random-Number Generator for Reproducibility

Function randrange actually generates pseudorandom numbers, based on an internal 
calculation that begins with a numeric value known as a seed. Repeatedly calling 
randrange 
produces a sequence of numbers that appear to be random, because each time you 
start a new interactive session or execute a script that uses the random module’s 
functions, Python internally uses a different seed value.1 When you’re debugging 
logic errors in programs that use randomly generated data, it can be helpful to 
use the same sequence of random numbers until you’ve eliminated the logic errors, 
before testing the program with other values. To do this, you can use the random
 module’s seed function to seed the random-number generator yourself—this forces 
 randrange to begin calculating its pseudorandom number sequence from the seed 
 you specify. In the following session, snippets [5] and [8] produce the same
  results, because snippets [4] and [7] use the same seed (32):

1According to the documentation, Python bases the seed value on the system 
clock or an operating-system-dependent randomness source. For applications 
requiring secure random numbers, such as cryptography, the documentation 
recommends using the secrets module, rather than the random module.
"""
