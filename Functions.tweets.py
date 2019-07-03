#import pandas
import pandas as pd

#import twitter data to dataframe
df = pd.read_csv("tweets.csv")

#initialize an empty dictionary : Langs_count
langs_count = {}

col = df['lang']

for entry in col:
    if entry in langs_count.keys():
        langs_count[entry] +=1
    else:
        langs_count[entry] = 1
print(langs_count)


