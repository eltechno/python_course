# Import pandas
import pandas as pd
from matplotlib import pyplot as plt
# Read the file into a DataFrame: df
df = pd.read_csv("literary_birth_rate.csv", sep=";")

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns, end="\n\n\n")

print(df.info())

print("frequency counts", df.fertility.value_counts(dropna=False))

print("frequency counts", df.population.value_counts(dropna=False).head())

print(df.describe())
# Print the head and tail of df_subset
#print(df_subset.head())
#print(df_subset.tail())

df.fertility.plot(kind='hist')
plt.show()

print(df[df.fertility > 2])

df.boxplot(column='fertility', by='Continent')
plt.show()