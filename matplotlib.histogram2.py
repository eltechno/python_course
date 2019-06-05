import numpy as np
import pandas as pd
globe =  pd.read_csv("gapminder.csv", skipinitialspace=True, usecols=['life_exp', 'gdp_cap', 'year'])
life_exp = list(globe.life_exp)
gdp_cap = list(globe.gdp_cap)
year = list(globe.year)


import matplotlib
#matplotlib.use("TkAgg") #this is only for macOS
from matplotlib import pyplot as plt


life_exp1950 = list(zip(year, life_exp))
print(life_exp1950[0])
life_exp19502 = np.array(life_exp1950)
print(life_exp19502, end="\n\n")


print(life_exp19502[0])

# Build histogram with 5 bins

plt.hist(life_exp, bins=5)
# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins

plt.hist(life_exp, bins=20)
# Show and clean up again
plt.show()
plt.clf()



