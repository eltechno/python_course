#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:50:14 2019

@author: techno
"""

name = "Paulo"
age = 41
sex = "man"

name2 = "Cesar"
age = 23
sex = "man"

name = "Tita"
age = 32
sex = "woman"

person1 = ['Paulo', 41, 'man']
person2 = ['Cesar', 23, 'man']
person3 = ['Tita', 32, 'woman']

guestList = [
        ['Paulo', 41, 'man'],
        ['Cesar', 23, 'man'],
        ['Tita', 32, 'woman']
        ]

print(guestList[1]) #imprime la lista 1 completa
print(guestList[1][2]) #imprime el elemento 3 de la sublista 1

guestList.append(['alfonso', 41,'men']) #agregar un nuevo record

print (guestList)

guestList2 = {
        ('Raul', 41, 'man'),  # tambien podemos asignar tuples
        ('Julio', 23, 'man'),
        ('Marta', 32, 'woman')
        }

guestList3 = {
        ('Roberto', 41, 'man'),  # tambien podemos asignar tuples
        ('Juliano', 23, 'man'),
        ('Marimar', 32, 'woman')
        }

#guestList2.append(['Ricardo', 41,'men']) #podemos agregar mas datos

print(guestList2)

guestList2.add(('sophie',21,'woman'))
print (guestList2)

guestList4 = guestList2 | guestList3
print (guestList4)