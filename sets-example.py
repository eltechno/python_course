#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:08:47 2019

@author: techno
"""

"""
        UNIQUE |    ORDER  | CHANGIN SPECIFIC ELEM. |   NEW ELEMENT
    
LIST       N           Y              Y                      Y
TUPLES     N           Y              N                      N
DICTIO     Y           N              Y                      Y
SETS       Y           N              N                      Y

          SETS HAVE BONUS OPERATIONS: | &  - ^
"""
#SETs for Unique elements

A = {40, -2, 20, 13} # un set es igual a un diccionario pero sin llave
print (A)

A.add (24) # agregar un dato a un SET
print (A) 

print (sorted(A)) # si se hace esto el SET se convierte en una lista

B = [4,4,4,4,3,2,54,6,7,8] #nueva lista
print ("Esta es la lista B, en SET", set(B)) # convierte una lista a un SET quitando los duplicados

A.discard(-2) #we can use A.remove as well
print (A)