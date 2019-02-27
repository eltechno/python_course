#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:34:48 2019

@author: techno
"""

""" LIST comprehensions (expressions/formulas)"""

numbers = [1, 2, 3, 4, 5, 6]

poweredNumbers = [] 

for elements in numbers:
        poweredNumbers.append(elements**2) #elevar los elementos de la lista a 
                                           #potencia de 2
print (numbers) 
print (poweredNumbers)

poweredNumbers2 = [element**2   #eleva a la potencia de 2
                 for element in numbers #de la lista numbers obtiene los datos para element
                 ]
print (poweredNumbers2)


"""
even number ends in 0,2,4,6,8 (par)
odd number ends in 1,3,5,7,9 (impar)
"""
evenNumbers = []
for items in numbers:
    if (items % 2 == 0):
        evenNumbers.append(items)
print (evenNumbers)
        
    
"""
[what_to_do_on_element | for element in old_list | condition_based_on_element]

element/item/entry
"""

evenNumbers2 = [element
                for element in numbers
                if (element % 2 == 0)
                ]
print (evenNumbers2 )


#no hay necesidad de colocar todos los numeros como en el ejemplo 
#de abajo numeros en rango de 0 a 20 + 1
poweredNumbers3 = [numeros**2   #eleva a la potencia de 2
                 for numeros in range(21) #de la lista numbers obtiene los datos para element
                 ]
print (poweredNumbers3)