#import pandas
import pandas as pd

#import twitter data to dataframe
tweets_df = pd.read_csv("tweets.csv")

#select RT from twitter Dataframe: result


result = filter(lambda x: x[0:2] =='RT', tweets_df['text'])

#create a list from object result: res_list

res_list = list(result)

print(res_list)