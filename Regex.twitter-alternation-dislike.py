import re

sentiment_analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.',
 "I disapprove the movie Honest with you. It's full of cliches.",
 'I dislike very much the concert After twelve Tour. The sound was horrible.']

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)

    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))