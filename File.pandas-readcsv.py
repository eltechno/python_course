import pandas as pd
filename = 'winequality-red.csv'
data = pd.read_csv(filename)
print(data.head())

data_array = data.values
print(data_array)