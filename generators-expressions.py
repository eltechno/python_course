#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

#squares_of_odds
for value in (x ** 2 for x in numbers if x % 2 !=0):
    print(value, end=' ')
print("")

def is_odd(x):
    """returns true only if x is odd"""
    return x % 2 != 0

print (list(filter(is_odd, numbers)))
print(list(filter(lambda x: x % 2 !=0, numbers)))

"""==========================================================="""

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False

"""filter function
The syntax of filter() method is:

[
filter(function, iterable)

"""
print (list(filter(filterVowels, alphabets)))


#filteredVowels = filter(filterVowels, alphabets)

#print('The filtered vowels are:')
#for vowel in filteredVowels:
#    print(vowel)