import pandas as pd
globe =  pd.read_csv("gapminder.csv", skipinitialspace=True, usecols=['life_exp', 'gdp_cap'])
life_exp = list(globe.life_exp)
gdp_cap = list(globe.gdp_cap)


import matplotlib
matplotlib.use("TkAgg") #this is only for macOS
from matplotlib import pyplot as plt


plt.hist(life_exp)
plt.show()
#this is how to show the graph