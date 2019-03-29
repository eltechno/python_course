#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

student_tuple = ('Amanda', 'blue', [98,75,87])
student_tuple[2][1] = 85 #changing the value for the 3rd of the list inside of the tuple
print(student_tuple)

first_name, color, grades = student_tuple
print(first_name)
print(grades)


"""-----------------------------------------------------------------------------------"""

first, second = 'hi'
print(f'{first} {second}')

number1, number2, number3 = [2,3,5]
print(f'{number1} {number2} {number3}')

number3 = 99
number4 = 22

number3, number4 = (number4, number3)
print(f'number3 = {number3}; number4= {number4}')
