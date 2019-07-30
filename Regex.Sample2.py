import re
sentiment_analysis = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

