#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:28:58 2019

@author: techno
"""


"""
# =============================================================================
# in 
# not in 
# operations in list
# =============================================================================
"""

names = ["juan","pedro","miguel","lorenzo","jacobo"] #5 elements
#          0       1      2          3         4

numbers = [1, 3, 51, 42, -5, 20] #six elements
#          0   1  2   3   4   5

numbers[5] = 30 # reemplazando el valor del index 5

print (numbers[5]) # visualizando el valor del index 5
print (names[-1])

for name in names: #ciclo para imprimir los index desde 0 a lo que contenga
    print (name)
    


print ("juan" in names) #check if some record in the list

if ("juan" in names): #condicional si tiene un record dentro del index
    print ("hola juan bienvenido")
    
if ("paulo" not in names): #condicional comprobar que no este dentro del index
    print ("paulo no se encuentra en la lista")