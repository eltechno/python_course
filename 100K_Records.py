#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 6/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # 100 k, sales records

import csv
from datetime import datetime
from time import sleep
import numpy as np
from collections import Counter

filename = "100000_Sales_Records.csv"
file = open(filename,newline="")
reader = csv.reader(file)
header = next(reader) # first line is the head
#print(header)

#lines = [line for line in open(filename)]
#for i in range(len(lines)):
#    print(lines[i])

datos = []
for row in reader:
    Region = row[0]
    Country = row[1]
    Item_Type = row[2]
    Sales_Channel = row[3]
    Order_Priority = row[4]
    Order_Date = datetime.strptime(row[5], '%m/%d/%Y')
    Order_ID = int(row[6])
    Ship_Date = datetime.strptime(row[7], '%m/%d/%Y')
    Units_Sold = int(row[8])
    Unit_Price = float(row[9])
    Unit_cost = float(row[10])
    Total_Revenue = float(row[11])
    Total_Cost = float(row[12])
    Total_Profit = float(row[13])
    datos.append([Region,Country,Item_Type,Sales_Channel,Order_Priority,Order_Date,Order_ID,Ship_Date,Units_Sold,Unit_Price,Unit_cost,
                  Total_Revenue,Total_Cost,Total_Profit])

Paises = [] #lista iniciandose
Solo_Nombres = [] #lista iniciandose
for i in range(len(datos)):
    #print(f'{datos[i][0]} , {datos[i][13]}')
    Paises.append([datos[i][0], datos[i][13]]) #Extrae solo primer campo pais y final total ventas
    Solo_Nombres.append(datos[i][0]) #llena lista con solo los nombres
mylist =list(dict.fromkeys(Solo_Nombres)) #convert a list into dictionary then a list again
#print (len(mylist))
#print(len(datos))
#print(len(Paises))

TEST=[]
for x in mylist:  #aqui el X toma el valor del pais, el STRING
    #print(x)
    #sleep(4)
    total = 0 #clear the total every iteration
    for y in range(len(Paises)):  # aqui y toma el valor de la cantidad de records
        #print(Paises[y][0])
        #print(x)
        if x == Paises[y][0]:
            #print(x)
            #sleep(4)
            #print(y, Paises[y][1])
            total = Paises[y][1] + total
    print(x, total) #print totales de cada region



#print(TEST)
#print(len(TEST))
#print(TEST)
