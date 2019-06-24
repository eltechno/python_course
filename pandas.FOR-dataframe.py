# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop little bit sophisticated

    for lab, row in cars.iterrows():
        print(lab + ": " + str(row["cars_per_cap"]))


# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = (row["country"].upper())

# Print cars
print(cars)


#another fast approach
# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
