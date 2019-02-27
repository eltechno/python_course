#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:18:23 2019

@author: techno
"""

# =============================================================================
# Break (leave the loop entirely)
# Continue (leave current iteration) repetition loop and continue
# =============================================================================

# =============================================================================
# result = 0
# 
# for i in range(3):
#     x = int(input("Enter a positive number: "))
#     if (x > 0):
#         result += x
#     else:
#         print("this is a negative number")
#         continue
#     print("*-*Current addition result =", result)
# =============================================================================

# =============================================================================
# para este programa while es mejor que for
# =============================================================================

result = 0
i = 0

while i < 4:
    x = int(input("Enter a positive number: "))
    if (x > 0):
        result += x
    else:
        print("this is a negative number")
        continue
# =============================================================================
# cuando un numero negativo aparece se ejecuta el print y vuelve al inicio 
# pero como no paso a la suma de i + 1 nunca, entonces el valor no se agranda
# y la condicion de while se mantiene hasta que exista un numero positivo        
# =============================================================================
    print("*-*Current addition result =", result)
    i += 1