

import pandas as pd
cereal_df = pd.read_csv("cereal.csv", skiprows=0, na_values = ['no info', '.'])
cereal_df2 = pd.read_csv("cereal2.csv")


# skiprow used to skip the headers or any other line upper the header
# na_values = ['no info', '.'] used Instead of parsing through each column
# and replacing 'no info' and '.' with NaN values after the dataset is loaded,
# you can use the na_values argument to account for those before it's loaded:

#are they the same?
print(pd.DataFrame.equals(cereal_df, cereal_df2))
print(cereal_df.head(5))


print(cereal_df['cups'].dtypes)
print(cereal_df['name'].dtypes)
print(cereal_df['fat'].dtypes)0
print(cereal_df['fat'][0])

print(cereal_df['fat'][0] + cereal_df['fat'][1])