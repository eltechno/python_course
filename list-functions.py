#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:37:46 2019

@author: techno
"""

"""
Python List Methods

append() - Add an element to the end of the list as SINGLE elements
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
max()
mix()
"""
names = ["juan","pedro","miguel","lorenzo","jacobo"] #5 elements
#          0       1      2          3         4

numbers = [1, 3, 51, 42, -5, 20, 3, 3] #six elements
#          0   1  2   3   4   5
number2 = [8, 9, 10]


numbers.sort() # ordena los numeros en forma ascendente
print (numbers)

numbers.sort(reverse=True) # ordena los numeros en forma descendente
print (numbers)

print (max(numbers)) # muestra el numero mas grande de la lista

print (min(numbers)) # muestra el numero mas pequenio de la lista

print ("hay",numbers.count(3)," numeros 3",) # cuenta cuantas veces 3 aparece en la lista
#x = len(names)
#print (x)
print (len(names))

numbers.pop() #remove the last element
print ("el ultimo numero fue removido", numbers)

numbers.remove(3) # remueve la primera ocurrencia del numero 3
print ("primer numero 3 removido", numbers)

numbers.reverse() #ordea en forma reversa el contenido de la lista
print ("lista en orden reverso", numbers)


numbers.append(99) # agrega un record al final de la lista
print (numbers)

numbers.extend(number2) #agrega una lista mas al final como elementos individuales
print (numbers)

numbers.append(number2) #agrega una lista mas al final como un solo record mas
print (numbers) # ver los brackets que coloca

numbers.insert(0,69) #inserta valor en la celda que le digamos
print (numbers)

print (numbers.index(51)) # muestra el numero de casilla que ocupa el numero en la lista


numbers.clear() #remueve todos los numeros de la lista
print ("se removieron todos los numeros", numbers)