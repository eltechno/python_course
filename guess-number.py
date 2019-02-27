#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:34:13 2019

@author: techno
"""
magicNumber = 40
userNumber = 0


while userNumber != magicNumber: 

# =============================================================================
#     userNumber = int(input("Please try to guess the magic number 10"))
#     if (userNumber == magicNumber):
#         print("you found the numerber")
#     else:
#         print ("try again")
# 
# =============================================================================

    userNumber = int(input("Please try to guess the magic number "))
    if (userNumber < magicNumber):
        print("its a little bit bigger")
    elif (userNumber > magicNumber):
        print ("its a little bit smaller")
    else:
        print("you found the numerber")

