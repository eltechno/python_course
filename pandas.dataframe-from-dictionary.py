

dict ={
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia","Moscow","New Delhi", "Beijing","Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population":[200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd

brics = pd.DataFrame(dict)

print(brics)


brics.index = ["BR", "RU", "IN", "CH", "SA"] #personalize the labels
print()

cols = "A B C D".split() #create new labels for columns
print(cols)   #print columns
print(brics.columns) #print(actual columns name)
brics.columns = cols  #replace the name with the new list
print()


brics.rename(columns={"C":"AREA"}, inplace=True) # replace only one name "C" for AREA

print(brics.info())


print(brics[["A", "AREA"]])
print(type(brics["A"]))


print(brics[1:4]) #print only rows

print()

print(brics.loc[["RU"]]) # only print one line with all the info

print("with loc",brics.loc[["RU", "IN", "CH"], ["A","D"]]) #specify what row and what columns
print("with iloc",brics.iloc[[1,2,3],[0,3]])

print("with loc",brics.loc[:,["A","D"]]) #al rows but only two columns
print("with iloc",brics.iloc[:,[0,3]]) #al rows but only two columns
print()


