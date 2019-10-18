#HDF5
#hierarchical Data Format Version 5

import h5py
import numpy as np
from matplotlib import pyplot as plt
filename = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename, 'r') # r is to read
print(type(data))

for key in data.keys():
    print(key)

print(type(data['meta']))

for key in data['meta'].keys():
    print(key)

print(data['meta']['Description'].value, data['meta']['Detector'].value)


#checking another group
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
