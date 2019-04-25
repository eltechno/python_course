#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

""" tokenizing a string and counting unique words"""

text = ('this is sample text with several words different '
        'this is more sample text with some different words')

word_counts = {}

#count ocurrences of each unique word

for word in text.split():
    if word in word_counts:
        word_counts[word] +=1 #update existing key-value pair
        print(word_counts) # print just to check how is working
    else:
        word_counts[word] = 1 #insert new key-value pair
        print(word_counts) # print just to check how is working
print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
print('\nNumer of unique words:', len(word_counts))


"""
Line 10 tokenizes text by calling string method split, which separates the 
words using the method’s delimiter string argument. If you do not provide 
an argument, split uses a space. The method returns a list of tokens 
(that is, the words in text). Lines 10–14 iterate through the list of words. 
For each word, line 11 determines whether that word (the key) is already 
in the dictionary. If so, line 12 increments that word’s count; otherwise, 
line 14 inserts a new key–value pair for that word with an initial count of 1.

Lines 16–21 summarize the results in a two-column table containing each word 
and its corresponding count. The for statement in lines 18 and 19 iterates 
through the diction-ary’s key–value pairs. It unpacks each key and value 
into the variables word and count, then displays them in two columns. 
Line 21 displays the number of unique words.
"""