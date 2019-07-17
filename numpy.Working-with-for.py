import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

for val in bmi:
    print(val)


meas = np.array([np_height,np_weight])

for val2 in meas:
    print(val2)

for val2 in np.nditer(meas):
    print(val2)