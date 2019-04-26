#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

"""Dictionary Method update
You may insert and update key–value pairs using dictionary method update.
First, let’s create an empty country_codes dictionary"""

country_codes = {}

"""The following update call receives a dictionary of key–value pairs to insert or update:"""

country_codes.update({'South   Africa': 'za'})
print(country_codes)

"""Method update can convert keyword arguments into key–value pairs to insert. 
The following call automatically converts the parameter name Australia into 
the string key 'Australia' and associates the value 'ar' with that key:"""

country_codes.update(Australia='ar')
print(country_codes)

"""provided an incorrect country code for Australia. Let’s correct this 
by using another keyword argument to update the value associated with 'Australia' """

country_codes.update(Australia='au')
print(country_codes)


"""Method update also can receive an iterable object containing 
key–value pairs, such as a list of two-element tuples."""

