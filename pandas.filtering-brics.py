
import pandas as pd
import numpy as np

brics = pd.read_csv("brics.csv", index_col=0)


print(brics)

#get the column for area only as pandas series not dataframe

print(brics["area"]) #single square brackets

brics.loc[:,"area"] #other option to get the same result
brics.iloc[:,2] #other option to get the same result


#now lets do the comparation

is_huge = (brics["area"] > 8)
print(is_huge)

print(brics[is_huge])

#another way to do the same
print(brics[brics["area"] > 8])

filter = np.logical_and(brics["area"] >8, brics["area"] < 10)

print("using variables")
print(brics[filter])

print("anothe way to include all in same line")
print(brics[np.logical_and(brics["area"] >8, brics["area"] < 10)])
