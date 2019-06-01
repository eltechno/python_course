# heights and positions are available as lists
import pandas as pd
fifa =  pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/fifa.csv", skipinitialspace=True, usecols=['position', 'height'])
positions = list(fifa.position)
heights = list(fifa.height)


# Import numpy

import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_height = np.array(heights)
np_positions = np.array(positions)


# Heights of the goalkeepers: gk_heights
gk_heights = np_height[np_positions == 'GK']
# Heights of the other players: other_heights
other_heights = np_height[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'

print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))