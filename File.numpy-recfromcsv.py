import numpy as np
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d

d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
