#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:28:07 2019

@author: techno
"""
#variables
VAT = 25 #IVA 
netPriceOfShoes = 100 #precio sin iva
netPriceOfTV = 2000 #precio sin iva

    # tambien se pueden declarar variables con ;
    # VAT = 25; netPriceOfShoes = 100; netPriceOfTV = 2000

calculatedVAT = (1  + VAT /100 ) #stored in RAM
# grossPriceOfShoes = netPriceOfShoes 
#* (1  + VAT /100 ) tambien 
#se puede expresar el calculo en una variable para no repetir 
#tanto



grossPriceOfShoes = netPriceOfShoes * calculatedVAT
grossPriceOfTV = netPriceOfTV * calculatedVAT

print (grossPriceOfShoes)
print (grossPriceOfTV)
#asignacion de variables por linea

#a,b,c = 1,2,3
#a = b = c = 1

a,b,c = 1,"test",True
print (a,b,c)

"""

+=      x += 5  its is a short way of writing: x = x + 5
-=      x -= 5  its is a short way of writing: x = x - 5
*=      x *= 5  its is a short way of writing: x = x * 5
/=      x /= 5  its is a short way of writing: x = x / 5
%=      x %= 5  its is a short way of writing: x = x % 5
//=      x //= 5  its is a short way of writing: x = x // 5
**=      x **= 5  its is a short way of writing: x = x ** 5

"""
