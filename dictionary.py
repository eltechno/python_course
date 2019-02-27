#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:53:00 2019

@author: techno
"""

#dictionary
"""
A dictionary is a collection which is unordered, 
changeable and indexed. In Python dictionaries are 
written with curly brackets, and they have keys 
and values.
"""
rooms = {49: 'Paulo Alvarado', 69: 'Cesar gonzalez' } #asi se crea un diccionario

#para modificar
rooms[49] = 'John Doe'

print (rooms)
rooms.update({555: 'Juan Perez', 68: 'Sergio Ramirez'})  # add another record to dictionary

print (rooms)

del (rooms[555]) # asi se remueve un record
print (rooms)

removedValue = rooms.pop(69)  # asi se remueve un record
print (rooms)
print ("elemento borrado",   removedValue)

print (rooms.popitem()) # borra ultimo registro y lo muestra junto con la key

print (len (rooms)) #longitud del diccionario

print (rooms.clear()) #borrar el contenido del diccionario