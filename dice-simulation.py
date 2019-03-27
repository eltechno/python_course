#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 25/03/19

#Feature:  #Enter feature name here
# Enter feature description here
"""
You roll two six-sided dice, each with faces containing one, two, three, four,
five and six spots, respectively. When the dice come to rest, the sum of the
spots on the two upward faces is calculated. If the sum is 7 or 11 on the
first roll, you win. If the sum is 2, 3 or 12 on the first roll
(called “craps”), you lose (i.e., the “house” wins).
If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your
“point.” To win, you must continue rolling the dice until you
“make your point” (i.e., roll that same point value).
 You lose by rolling a 7 before making your point.
"""
#Scenario:  # Enter scenario name here
# Enter steps here
import random

def roll_dice():
    """ Roll two dice and return their face values as tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)

def display_dice(dice):
    """display one roll of the two dice ."""
    die1, die2 = dice #unpack the tuple in to variables die1 and die2
    #print(dice) #this is the tuple
    print (f'Player Rolled {die1} + {die2} = {sum(dice)}')


die_values = roll_dice() #first roll
display_dice(die_values)
sum_of_dice = sum(die_values) #determine game status and point based on the first roll

if sum_of_dice in (7, 11): #win
    game_status='WON'
elif sum_of_dice in (2,3,12): #Lose
    game_status='LOST'
else: #remember point
    game_status= 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

while game_status =='CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    if sum_of_dice == my_point: # win by making point
        game_status = 'WON'
    elif sum_of_dice == 7: #lose by rolling 7
        game_status ='LOST'

#display "wins" or "loses" message
if game_status =='WON':
    print("Player Wins")
else:
    print("Player Loses")