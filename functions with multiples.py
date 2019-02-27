""" functions with multiple parameter
area of the rectangle

side1 and side2
"""

def areaRectagle(side1, side2):
    print ("Area of the rectagle",side1 * side2)

areaRectagle(2,8)

numero = areaRectagle(2,4)
print (numero)

#Returning values from a function

def areaRectagle2(side1, side2):
    return (side1 * side2) # return will provide the real value of the function

print (5 * areaRectagle2(2,4))


def divide(a,b):
    if (b== 0):
        return
    return a /b

print (divide(20,0))

if (divide(20,0)):
    print ("done")
else:
    print("Division by zero")
