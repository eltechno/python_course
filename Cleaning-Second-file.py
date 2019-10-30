import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("dob_job_application_filings_subset.csv.1",dtype={"Adult Estab": object})

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns)
print(df.Borough.value_counts(dropna=False).head())

print(df.describe())

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

df.Block.plot(kind='hist')
plt.show()