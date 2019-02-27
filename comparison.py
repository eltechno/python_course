#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:43:38 2019

@author: techno
"""
"""
< 	strictly less than
<= 	less than or equal
> 	strictly greater than
>= 	greater than or equal
== 	equal
!= 	not equal
is 	object identity
is not 	negated object identity


conditional statements
PSEUDO CODE

if (true/nottrue)
 ...
elseif(true/nottrue)
 ...
elseif(true/nottrue)
 ...
else
 ...

person = input("Nationality? ")
if person == "french" or person == "French" :
    print("Préférez-vous parler français?")
elif person == "italian" or person == "Italian": #si lo anterior no es cierto
    print("Preferisci parlare italiano?")
else: #si todo lo anterior no se cumple
    print("You are neither Italian nor French,")
    print("so we have to speak English with each other.")

"""

a = int(input("first number")) #
b = int(input("second number"))

if (a > b):
    print(a,"is grater than", b)
elif(a < b):
    print(a," is lower than",b)
else:   
    print(a," is equal to",b)
    