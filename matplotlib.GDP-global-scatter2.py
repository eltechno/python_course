
import pandas as pd
globe =  pd.read_csv("gapminder.csv", skipinitialspace=True, usecols=['life_exp', 'population'])
life_exp = list(globe.life_exp)
pop = list(globe.population)



import matplotlib
matplotlib.use("TkAgg") #this is only for macOS
from matplotlib import pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

plt.xscale('log')

# Show plot
plt.show()
