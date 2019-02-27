#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:50:32 2019

@author: techno
"""

"""
Write a program that will allow the user to:
1) Add new definitions
2) Search existing definitions
3) Delete the definition that he has chosen
TAB
"""
dictionary = {}

while (True):
    print ("1: Add Definition")
    print ("2: Search for Definition")
    print ("3: Remove Definition")
    print ("4: Display the content")
    print ("5: End")
    choice = input("What you want to do?..")
    
    if(choice == "1"):
        key = input("Enter the work (key) to define: ")
        definition = input ("Enter definition ")
        dictionary[key] = definition
        print ("Definition added successfully")
    
    elif (choice == "2"):
        key = input("Enter the key to search: ")
        if key in dictionary:
            print ("the key is: ", dictionary[key])
            print()
        else:
            print("the key ",key," is not found")
            
    elif (choice =="4"):
        for x in dictionary:
            print(x,": ", dictionary[x])
        print()
        
    elif (choice =="3"):
        key = input("Enter the key to delete: ")
        if key in dictionary:
            del dictionary[key]
            print ("definition", key, "has been removed")
        else:
            print ("key not found")
    elif (choice =="5"):
        print ("Exiting...")
        break
            

