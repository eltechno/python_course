import figures

#test = figures.area_of_square(10)
#print (test)

#test2 = figures.area_of_circle(4.5)
#print (test2)


while (True):
    choose = input(""" What figures area you want to measure
    1. Square
    2. Rectangle
    3. Circle
    4. Triangle
    5. Trapezee
    6. exit
    """)
    if (choose == '1'):
        a = float(input("enter the size of the square side :"))
        print ("the areas is: ",figures.area_of_square(a))

    elif  (choose == '2'):
        a = float(input("enter the size of the rectangle side a:"))
        b = float(input("enter the size of the rectangle side b:"))
        print ("the areas is: ",figures.area_of_rectangle(a,b))

    elif  (choose == '3'):
        r = float(input("enter the size of the Radio of the circle:"))
        print ("the areas is: ", figures.area_of_circle(r))

    elif  (choose == '4'):
        b = float(input("enter the size of the base : "))
        h = float(input("enter the size of the height : "))
        print ("the areas is: ", figures.area_of_triangle(b,h))

    elif  (choose == '5'):
        a = float(input("enter the size of the upper base : "))
        b = float(input("enter the size of the lower base : "))
        h = float(input("enter the size of the height : "))
        print ("the areas is: ", figures.area_of_trapeze(a,b,h))

    elif (choose =="6"):
        print ("Exiting...")
        break