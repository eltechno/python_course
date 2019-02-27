"""
    Function - is a block of code that you can access any time
               to get the result you want


    def name_of_function():
        instruction1
        instruction2
        instruction3

    definition
    parameter
"""

def welcome(name): #siempre se tiene que declarar la variable a usar o en la que se coloca el parametro
    print("welcome to this work my friend",name, "!!!!")

welcome("Paulo") # la funcion se ejecuta con el parametro nombre

for x in range(1, 10):
    welcome(x)

names = ["Paulo", "Cesar", "Alvarado", "Raul"]
for items in names:
    welcome(items)
