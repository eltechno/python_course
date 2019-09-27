import pandas as pd

#pandas can read datetime objects
# need to specify "parse_date=True"
# Date ISO format 8601


sales = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')
print(sales.info())
print(sales.head(), end="\n\n")

#search of specific date and time
print(sales.loc['2015-02-19 10:59:33'], 'Company')

#search for one day
print(sales.loc['2015-02-5'])

#search with partcial datetime string selection
# Alternative formats:
# sales.loc['February5, 2015']
# sales.loc['2015-Feb-5']
#whole month: sales.loc['2015-02']
#whole year: sales.loc['2015']

print(sales.loc['2015-02'])

#slicing using date /times

print(sales.loc['2015-2-16' : '2015-2-20'])

#convert strings to datetime
everning_2_11 = pd.to_datetime(['2015-2-11 20:00', '2015-2-11 21:00','2015-2-11 22:00', '2015-2-11 23:00'])
print(everning_2_11)

#reindexing dataframe
# df.reindex(new_index, fill_value=0)
# df2.reindex(date_index2, method='bfill')
print(sales.reindex(everning_2_11))


#Filling missing values
#method forward fill ffill
#method backward fill bfill

#sales.reindex(everning_2_11, method='ffill')


# Prepare a format string: time_format
#time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
#my_datetimes = pd.to_datetime(date_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
#time_series = pd.Series(temperature_list, index=my_datetimes)

