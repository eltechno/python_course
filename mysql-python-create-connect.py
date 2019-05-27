#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 13/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import mysql.connector
#conda install -c anaconda mysql-connector-python

connection = mysql.connector.connect(host ="127.0.0.1",user="techno",password="Guate2019_")
#connection is the string to connect to database

mycursor = connection.cursor()

#mycursor.execute("DROP DATABASE pydata") #drop databases
#mycursor.execute("CREATE DATABASE pydata") # create a database
mycursor.execute("SHOW DATABASES")


for x in mycursor: #lista las bases de datos
    print(x)

connection.close() #close the conection

