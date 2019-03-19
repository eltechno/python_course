#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 18/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

sample_1= "some_name = the value"
for position in range(len(sample_1)):
    if sample_1[position] in "=:":
        print("position: ", position, "del caracter", sample_1[position])
        break
