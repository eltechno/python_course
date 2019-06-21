

fam = [1.73, 1.68, 1.71, 1.89]

for index, height in enumerate(fam):
    print("index " + str(index) + ": " + str(height))






# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house:
    print("the " + x[0] + " is " + str(x[1]) + " sqm")