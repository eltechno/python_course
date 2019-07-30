import pandas as pd
import re
my_dataframe = pd.read_csv("short_tweets.csv", usecols=["text"])
#filter only the last description
#wikipedia_article = my_dataframe.iloc[3,0]
#print(my_dataframe)

#here converting the pandas datafrase into pandas series
twitter = my_dataframe.text

# Complete the for loop with a regex to find dates
#similar to 27 minutes ago or 4 hours ago

for date in twitter:
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for loop with a regex to find dates
#23rd june 2018
for date1 in twitter:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date1))

# Complete the for loop with a regex to find dates
#1st september 2019 17:25.
for date in twitter:
	print(re.findall(r"\d{2}\w\s\w+\s\d{4}\s\d{1,2}:\d{1,2}", date))