"""
Write a program that will count the sum of all numbers from 1 to number that was entered by user.
"""

def sum_up_to (numberToCount):
    sum = 0
    for items in range (1, numberToCount + 1):
       sum = sum + items
    return (sum)

def sum_up_to2 (numberToCount):  #otro metodo para hacer lo mismo
    return sum([number for number in range (1, numberToCount + 1)]) #list comprenhention

def sum_up_to3 (numberToCount):  #otro metodo para hacer lo mismo
    return sum({number for number in range (1, numberToCount + 1)}) #set comprenhention

def sum_up_to4 (numberToCount):  #otro metodo para hacer lo mismo
    return sum((number for number in range (1, numberToCount + 1))) #generator


counting = int (input("Hasta que numero quiere contar"))
print (sum_up_to(counting))

print (sum_up_to2(100))

"""
sum from 1 to  5 when the different between each number is the same
 (first number  + last number ) / 2 * (amount of elements)
"""

