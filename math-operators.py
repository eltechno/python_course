#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here


"""
Union
The union of two sets is a set consisting of all the unique elements
from both sets. You can calculate the union with the |
operator or with the set type’s union method:
"""
print({1, 3, 5} | {2, 3, 4})
print( {1, 3, 5}.union([20, 20, 3, 40, 40]))

"""
The operands of the binary set operators, like |, must both be sets. 
The corresponding set methods may receive any iterable object as an
argument—we passed a list. When a mathematical set method receives 
a non-set iterable argument, it first converts the iterable to a set, 
then applies the mathematical operation. Again, though the new sets’
string representations show the values in ascending order, you 
should not write code that depends on this
"""

"""
Intersection

The intersection of two sets is a set consisting of 
all the unique elements that the two sets have in 
common. You can calculate the intersection with 
the & operator or with the set type’s intersection 
method
"""
print({1, 3, 5} & {2, 3, 4})
print({1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4]))

"""
Difference

The difference between two sets is a set consisting 
of the elements in the left operand that are not in 
the right operand. You can calculate the difference 
with the - operator or with the set type’s difference 
method:
"""
print({1, 3, 5} - {2, 3, 4})
print({1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4]))

"""
Symmetric Difference

The symmetric difference between two sets is a set 
consisting of the elements of both sets that are 
not in common with one another. You can calculate 
the symmetric difference with the ^ operator or 
with the set type’s symmetric_difference method:
"""
print({1, 3, 5} ^ {2, 3, 4})
print({1, 3, 5, 7}.symmetric_difference([2,   2, 3, 3, 4, 4]))

"""
isjoint

Two sets are disjoint if they do not have any 
common elements. You can determine this with 
the set type’s isdisjoint method:
"""
print({1, 3, 5}.isdisjoint({2, 4, 6}))
print({1, 3, 5}.isdisjoint({4, 6, 1}))


"""
Mutable Mathematical Set Operations
Like operator |, union augmented assignment |= performs a set union operation, but |= modifies its left operand:
"""
numbers = {1, 3, 5}

numbers |= {2, 3, 4}

print(numbers)


"""
Similarly, the set type’s update method performs a union 
operation modifying the set on which it’s called—the 
argument can be any iterable:
"""

numbers.update(range(10))
print(numbers)


"""
The other mutable set methods are:
intersection augmented assignment &=
difference augmented assignment -=
symmetric difference augmented assignment ^=
and their corresponding methods with iterable arguments are:
-intersection_update
-difference_update
-symmetric_difference_update
Methods for Adding and Removing Elements

Set method add inserts its argument if the argument is not already in the set; otherwise, the set remains unchanged:
"""
numbers.add(17)
numbers.add(3)
print(numbers)


"""
Set method remove removes its argument from the set—a KeyError occurs if the value is not in the set:
"""
numbers.remove(3)
print(numbers)

"""
Method discard also removes its argument from the set but 
does not cause an exception if the value is not in the set.

You also can remove an arbitrary set element and return
 it with pop, but sets are unordered, so you do not 
 know which element will be returned:
"""

numbers.pop()
print(numbers)

"""
A KeyError occurs if the set is empty when you call pop.
Finally, method clear empties the set on which it’s called:
"""
numbers.clear()

print(numbers)
set()

"""
6.3.4 Set Comprehensions

Like dictionary comprehensions, you define set comprehensions in curly braces.
 Let’s create a new set containing only the unique even values in the list numbers:
"""

numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
evens = {item for item in numbers if item % 2 == 0}
print(evens)
