

import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)


for val in brics:
    print(val)


for lab, row in brics.iterrows():
    print(lab)
    print(row, end="\n\n")


#add a new tab usind data from the same dataframe
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics, end="\n\n")

#another way to do the same len calculation

brics["name_lenght2"] = brics["country"].apply(len)
print(brics)
