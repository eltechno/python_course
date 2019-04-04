#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 2/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

full_name = lambda fn, ln: fn.lower().strip().title() + " " + ln.lower().strip().title()
print("Printing with Lambda :" , full_name("quEndal", "Marica"))

def fullname(fn, ln):
    fn.lower().strip().title() + " " + ln.lower().strip().title()
print("Printing with function : ", full_name("quEndal", "mARICA"))


scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert heinlein", "Arthus C. Clarke", "Frank herbert", "Orson Scoot Card",
                 "Douglas Adams","H. G. Wells", "Leigh Brackett"]

#the -1 means the split will start and the end of the name
#list.sort(reverse=True|False, key=myFunc)
scifi_authors.sort(reverse=True, key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

def build_quadratic_func(a,b,c):
    """ Returns the function f(x) = ax^2 + bx + c """
    return lambda x: a*x**2 + b*x + c
f = build_quadratic_func(2,3,-5)
print(f(0))

f = build_quadratic_func(3,0,2)
print(f(2))
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print (list(filter(lambda x: x % 2 !=0, numbers)))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26),
         ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijin", 32)]
""" list of temperatures in Celcuis"""

c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
print("hecho automatico",list(map(c_to_f, temps)))



def temperatura(y):
    return (((9/5)*y) +32)
#print only one record
#print(temperatura(temps[0][1]))
listado = []
for citi, temp in temps:
    #print(list((citi, (temperatura(temp)))))
    b = temperatura(temp)
    listado.append((citi,b))
print("hecho a mano", listado)
