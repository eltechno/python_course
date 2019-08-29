import pandas as pd
heights = [59.0, 55.2, 64.4, 65.4, 63.7, 64.1, 70.1]

data ={'height' : heights, 'sex' : 'M'}
result = pd.DataFrame(data)
print(result)

#you can chage the index and columns using the below attributes
result.columns =['Height (in)' , 'sex']
result.index=['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(result)