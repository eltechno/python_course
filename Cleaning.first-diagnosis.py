# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv("nyc_uber_2014.csv")

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
#print(df_subset.head())
#print(df_subset.tail())
