import pandas as pd
df = pd.read_csv("auto-mpg.csv")

total = df[df['origin'] == 'Asia'].count()
#print(total)

global_mean = df.mean()
global_std = df.std()

us = df[df['origin'] == 'US']

us_mean = us.mean()
us_std = us.std()

print(us_mean - global_mean)
print(us_std - global_std)

