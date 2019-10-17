import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_stata('disarea.dta')
print(data)


# Print the head of the DataFrame df
print(data.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(data[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()