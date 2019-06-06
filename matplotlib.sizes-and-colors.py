import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
globe =  pd.read_csv("gapminder.csv", skipinitialspace=True, usecols=['life_exp', 'gdp_cap', 'population','cont'])
life_exp = list(globe.life_exp)
gdp_cap = list(globe.gdp_cap)
pop = list(globe.population)
continent = list(globe.cont)


dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

col = [dict[x] for x in continent] # here we can assing colors to each continent



# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
np_pop = np_pop / 1000000 #resize the data into millons




# Double np_pop


# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop * 2, c = col, alpha=0.8 )

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()