
import pandas as pd
globe =  pd.read_csv("gapminder.csv", skipinitialspace=True, usecols=['life_exp', 'gdp_cap'])
life_exp = list(globe.life_exp)
gdp_cap = list(globe.gdp_cap)



import matplotlib
#matplotlib.use("TkAgg") #this is only for macOS
from matplotlib import pyplot as plt

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()