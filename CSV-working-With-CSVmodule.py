#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 3/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import csv
path = "Google_Stock_ Market_Data - google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # first line is the head
data = [row for row in reader] #read the remaining data

print (header)
print(data[0])

