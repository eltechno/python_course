#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 18/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
import os

#get the pwd
print (os.getcwd())
os.chdir("/home/techno/Documents")
print(os.getcwd())

#split the path in two variables
pathName = os.getcwd()
print (os.path.split(pathName))
dirname1, dirname2  = os.path.split(pathName)
print (os.path.split(dirname1))
print (dirname2)

#split filename and extension from OS path
pathname2 = '/home/techno/Documents/python/get_password.py'
print (os.path.split(pathname2))
directory, file = os.path.split(pathname2)
filename, extension = os.path.splitext (file)
print (filename)
print (extension)

#get the directory content
import glob
os.chdir('/home/techno/Documents')
print (glob.glob('python/*.py'))

