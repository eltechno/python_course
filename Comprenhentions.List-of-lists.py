# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for col in range(0,4)]

# Print the matrix
for row in matrix:
    print(row)


print ([num **2 for num in range(10) if num % 2 == 0])

#conditional on the ouput expression
print ([num **2 if num % 2 == 0 else 0 for num in range(10) ])

