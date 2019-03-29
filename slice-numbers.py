#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 29/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

#Specifying a Slice with Starting and Ending Indices
#Let’s create a slice consisting of the elements at indices 2 through 5 of a list:

numbers = [2,3,5,7,11,13,17,19]
print(numbers[2:6])


#Specifying a Slice with Only an Ending Index
#If you omit the starting index, 0 is assumed. So, the slice numbers[:6] is equivalent to the slice numbers[0:6]:
print(numbers[:6])

print(numbers[6:len(numbers)])

print(numbers[6:])


print(numbers[::2])

#Modifying Lists Via Slices
#You can modify a list by assigning to a slice of it—the rest of the list is unchanged.
# The following code replaces numbers’ first three elements, leaving the rest unchanged:

numbers[0:3] = ['two', 'three', 'five']
print (numbers)

#The following deletes only the first three elements of numbers by assigning an empty list to the three-element slice:
"""numbers[0:3] = []
print(numbers) """


#The following assigns a list’s elements to a slice of every other element of numbers:
numbers[::2] = [100,100,100,100]
print (numbers)

#Let’s delete all the elements in numbers, leaving the existing list empty:
numbers[:] = []
print(numbers)
print(id(numbers))

#Deleting numbers’ contents (snippet [19]) is different from assigning numbers a
# new empty list [] (snippet [22]). To prove this, we display numbers’ identity
# after each operation. The identities are different, so they represent separate
# objects in memory:
numbers = []
print(numbers)
print(id(numbers))