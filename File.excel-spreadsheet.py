import pandas as pd
file = 'urban_pop_orig.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)

df1 = data.parse("Data") #parse the excel sheet called data
df2= data.parse(0) #parse the index sheet # 0

print(df1)