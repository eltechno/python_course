#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

""" using a dictionary  to represent an instructor's grade book"""
grade_book ={
    'Susan': [92, 85, 100],
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],
    'Pantipa': [97, 91, 92]
}
all_grades_total=0
all_grades_count=0

for names, grades in grade_book.items():
    total = sum(grades)
    print(f'Averange for {names} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")
