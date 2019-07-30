import pandas as pd
import re
my_dataframe = pd.read_csv("short_tweets.csv", usecols=["text"])
#filter only the last description
#wikipedia_article = my_dataframe.iloc[3,0]
#print(my_dataframe)

#here converting the pandas datafrase into pandas series
twitter = my_dataframe.text

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
#no_hashtag = re.sub(r"#\w+","O", my_dataframe)

for tweet in twitter:
    print(re.sub(regex,"", tweet))

sentiment_analysis = "ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever"
# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))