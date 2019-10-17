#sas and stata files
# SAS statistical Analisys System

# Stata: Statistic + data

import pandas as pd
from matplotlib import pyplot as plt

from sas7bdat import SAS7BDAT
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

print(df_sas.head())


#plot histogram of dataframe features

pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()