import pandas as pd

#pandas can read datetime objects
# need to specify "parse_date=True"
# Date ISO format 8601


sales = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')
print(sales.info())
