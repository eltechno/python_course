#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:58:29 2019

@author: techno
"""

"""
There are four collection data types in the Python programming language:

List    []       is a collection which is ordered and changeable. Allows duplicate members.
Tuple   ()       is a collection which is ordered and unchangeable. Allows duplicate members.
Set     {}       is a collection which is unordered and unindexed. No duplicate members.
Dictionary   {}  is a collection which is unordered, changeable and indexed. No duplicate members.



"""

#generator of expressions are in use with big amount of data to be processed

import sys

#comprenhention list
evenNumbers = [element
               for element in range(401)
               if (element % 2 == 0)
               ]
print (evenNumbers)

#generator of expressions
evenNumbersGenerator = (element
               for element in range(401)
               if (element % 2 == 0)
               )
#generator of expressions
print (evenNumbersGenerator)

print (next (evenNumbersGenerator))

#for number in evenNumbersGenerator: #imprime el contenido de el generador
#    print (number)

print (sys.getsizeof(evenNumbers)) #get the size in memory
print (sys.getsizeof(evenNumbersGenerator))  #get the size in memory


