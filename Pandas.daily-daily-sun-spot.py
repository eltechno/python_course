#CSV file has no columns headers
    # Column 0-2 Gregorian data(year, month, day)
    # Column 3 Date as fraction as year
    # Column 4 Daily total sunpost number
    # Column 5 Definitive/provisional indicator(1/0)
#missing values in column 4 indicated by -1
#dates representation inconvenient

import pandas as pd
filepath  = 'ISSN_D_tot.csv'
col_name = ['year','month', 'day', 'dec_date', 'sunspots', 'definite']
#sunspots = pd.read_csv(filepath, header=None, names=col_name, na_values=' -1')
sunspots = pd.read_csv(filepath, header=None, names=col_name, na_values={'sunspots':[' -1']},
                       parse_dates=[[0,1,2]])
#the CSV files the -1 value have a blank space at the begining
sunspots.info()
print(sunspots.iloc[10:20, :])

sunspots.index = sunspots['year_month_day']
sunspots.index.name = 'date'
sunspots.info()

cols= ['sunspots', 'definite']
sunspots= sunspots[cols]
print(sunspots.iloc[10:20, :])

out_csv='sunspots.csv'
sunspots.to_csv(out_csv)

out_tsv='sunspots.tsv'
sunspots.to_csv(out_tsv, sep='\t')

out_xlsx = 'sunspots.xlsx'
sunspots.to_excel(out_xlsx)