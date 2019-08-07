import re

sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!',
 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.',
 "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))