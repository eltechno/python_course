import re
sentiment_analysis = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))