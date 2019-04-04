#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 1/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
"""
The preceding chapter introduced the function-call stack.
Python does not have a built-in stack type, but you can think
of a stack as a constrained list. You push using list method
append, which adds a new element to the end of the list.
You pop using list method pop with no arguments,
which removes and returns the item at the end of the list.

Let’s create an empty list called stack, push (append)
two strings onto it, then pop the strings to
confirm they’re retrieved
in last-in, first-out (LIFO) order:

"""
stack = []

stack.append('red')
stack.append('green')

print(stack)
stack.pop()
print(stack)

stack.pop()
print(stack)

