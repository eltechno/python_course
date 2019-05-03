#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 3/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

path = "Google_Stock_ Market_Data - google_stock_data.csv"
#fileopen = open(path)
#for line in fileopen:
    #print(line)

lines = [line for line in open(path)] #list comprenhention
#print(lines[0])
#print(lines[0].strip())
#print(lines[0].split(','))

dataset = [line.strip().split(',') for line in open(path)] #list comprenhention
print(dataset[0])
print(dataset[2])

