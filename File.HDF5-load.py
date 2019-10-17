#HDF5
#hierarchical Data Format Version 5

import h5py
filename = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename, 'r') # r is to read
print(type(data))

for key in data.keys():
    print(key)

print(type(data['meta']))

for key in data['meta'].keys():
    print(key)

print(data['meta']['Description'].value, data['meta']['Detector'].value)