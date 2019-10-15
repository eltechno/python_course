import numpy as np

data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

print(np.shape(data))

print(data['Survived'])