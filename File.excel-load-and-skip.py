import pandas as pd

file = "battledeath.xlsx"
xls = pd.ExcelFile(file)

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())


"""
Parse the first sheet by index. In doing so, 
skip the first row of data and name the columns 
'Country' and 'AAM due to War (2002)' using the 
argument names. The values passed to skiprows 
and names all need to be of type list.


Parse the second sheet by index. In doing so, 
parse only the first column with the usecols 
parameter, skip the first row and rename the 
column 'Country'. The argument passed to 
usecols also needs to be of type list.
"""