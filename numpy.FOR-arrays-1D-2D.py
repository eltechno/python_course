# np_baseball is available

# Import numpy
import pandas as pd
baseball = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv", skipinitialspace=True, index_col=1, usecols=['Height', 'Weight'])
height = list(baseball.Height)



# Import numpy as np
import numpy as np

np_height = height
np_baseball = baseball

# For loop over np_height

for x in np_height:
    print(x ,"inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)