#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:03:06 2019

@author: techno
"""

name="Paulo"
#     01234  asi cuenta las palabras en python
lastName="Alvarado"

#fullName = name + lastName
fullName = name +" " + lastName

print(fullName)

longString = "this is a text what was taken from somewhere this is a text what was taken from somewherethis is a text what was taken from somewhere" 
print(longString)

#podemos usar \ para separar lineas en el editor
longStringTwo = "this is a text what was taken from\
 somewhere this is a text what was taken from somewhere\
 this is a text what was taken from somewhere" 

print(longStringTwo)

#podemos usar """ para separar lineas en el editor
longStringTwo = """this is a text what was taken from
 somewhere this is a text what was taken from somewhere
 this is a text what was taken from somewhere"""

print(longStringTwo)

#strings as array of letters

print (name[0]) #print the frist letter of the name
print (name[-1]) #print the last letter of the name
print (name[1:]) #print all except for the first letter
print (name[:3]) #print todo hasta la tercera posicion sin incluirla
print (name[0:1]) #print todo hasta la primera linea sin incluirla



