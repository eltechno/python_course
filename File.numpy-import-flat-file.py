import numpy as np
filename = 'mnist_kaggle_some_rows.csv'
data = np.loadtxt(filename, delimiter=',')
#data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols[0,2])
#data = np.loadtxt(filename, delimiter=',', dtype=str)
print(data)

