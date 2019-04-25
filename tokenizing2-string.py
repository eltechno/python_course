#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

from collections import Counter

text = ('this is sample text   with several words '
        'this is more sample   text with some different words')

counter = Counter(text.split())
#print(counter)

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
print('Number of unique   keys:', len(counter.keys()))

"""
Snippet [3] creates the Counter, which summarizes the list 
of strings returned by text.split(). In snippet [4], 
Counter method items returns each string and its associated 
count as a tuple. We use built-in function sorted to get a 
list of these tuples in ascending order. By default sorted 
orders the tuples by their first elements. If those are 
identical, then it looks at the second element, and so on. 
The for statement iterates over the resulting sorted list, 
displaying each word and count in two columns.
"""