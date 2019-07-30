import pandas as pd
import re
my_dataframe = pd.read_csv("short_tweets.csv", usecols=["text"])
#filter only the last description
#wikipedia_article = my_dataframe.iloc[3,0]
#print(my_dataframe)

#here converting the pandas datafrase into pandas series
twitter = my_dataframe.text
#print(type(twitter))

for tweet in twitter:
	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))
	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+\d", tweet))