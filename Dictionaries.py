#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 10/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
#You can create an empty dictionary with {}.
#A dictionary is an unordered collection which stores #
# key–value pairs that map immutable keys to values,
# just as a conventional dictionary maps words to
# definitions. A set is an unordered collection
# of unique immutable elements.

country_codes = {'Finland':   'fi', 'South Africa':   'za', 'Nepal':   'np'}
print(len(country_codes))

if country_codes:
    print('country code is not empty')
else:
    print('country code is empty')

post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "Language": "English", "daatetime":"20230215T124231Z", "location":(44.590533, -104.7155556)}
print(post)

#creating dictonay with DICT function
post2 = dict (message ="SS cotopaxi", language="English")

#adding values
post2["user_id"] = 209
post2["datetime"] = "19771116T"

print(post2)

print("this the message in post dictionary", post["message"])


if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value")

#this is another way to handle the keyerror
try:
    print(post2['location'])
except KeyError:
    print("The post does not have location")

print(dir(post2))

print(help(post2.get))

loc = post2.get('location', None)
print(loc)


for key in post.keys():
    value = post[key]
    print(key,"=", value)

print()

for key, value in post.items():
    print(key,'=', value)

days_per_month = {'January':   31, 'February': 28, 'March': 31}

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

print()

roman_numerals = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
#get the value associated with the key 'V'
print(roman_numerals['V'])

#lets correct the key X with the correct value
roman_numerals['X'] = 10
print(roman_numerals)

#adding new pair of key and value
roman_numerals['L']= 50
print(roman_numerals)

#deleting a key value pair
del roman_numerals['III']
print(roman_numerals)

#deleting a key value pair with pop
roman_numerals.pop('X')
print(roman_numerals)

#print(roman_numerals['III'])

#if no other settings is apply no message display or only None
print(roman_numerals.get('III'))

print(roman_numerals.get('III', 'III not in dictionary'))

print(roman_numerals.get('V'))

#Testing Whether a Dictionary Contains a Specified KeyOperators in and not in can
# determine whether a dictionary contains a specified key:

print ('V' in roman_numerals)
print ('III' in roman_numerals)
print ('III' not in roman_numerals)


months = {'January': 1, 'February': 2, 'March': 3}

for day, month_name in months.items():
    print(day, month_name, end="  ")
print()

for month_name in months.keys():
    print(month_name, end=" ")
print()

for month_number in months.values():
    print(month_number, end=" ")
print()

#Converting Dictionary Keys, Values and Key–Value Pairs to Lists
print ( list(months.keys()) )
print ( list(months.values()) )

print(list(months.items()))
print()

#Processing Keys in Sorted Order
for months_name in sorted(months.keys()):
    print(months_name, end=" ")

print()

#Dictionary Comparisons
country_capitals1 = {'Belgium':   'Brussels','Haiti':   'Port-au-Prince'}
country_capitals2 = {'Nepal':   'Kathmandu','Uruguay':   'Montevideo'}
country_capitals3 = {'Haiti':   'Port-au-Prince', 'Belgium':   'Brussels'}

print (country_capitals1 == country_capitals2)
print(country_capitals1 == country_capitals3)
print(country_capitals1 != country_capitals2)

