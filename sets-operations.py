#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:12:52 2019

@author: techno
"""

"""
SETS have Bonus operations: | & - ^
| UNION
& INTERSECTION
- DIFERENCE
^ XOR EXCLUSIVE OR (REMOVING INTERSECTION FROM UNION)
"""

A = {-2, 10, 40, 20}
B = {4, 7, 10 ,20}

print (A|B) #unir dos sets
print (A.union(B)) # esta es otra forma de unir en ligar de pipe
print ("dos sets unidos y ordenados", sorted(A|B))

print ("muestra solo los valores questan en ambos sets", A&B)
print (A.intersection(B)) # esta es otra forma de hacer la interseccion


print ("muestra los valores unicos entra a y b", A-B) # unicamente muestra los valores que no existen en B y son de A
print ("muestra los valores unicos entra a y b", B-A) # unicamente muestra los valores que no existen en a y son de B

print (A^B) # remueve los repetidos y no muestra ninguno que no sea unico
