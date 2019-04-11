#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 9/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
minimo = min(colors, key=lambda s: s.lower())
print (minimo)

maximo = max(colors, key=lambda s: s.lower())
print (maximo)
