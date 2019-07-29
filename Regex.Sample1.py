#Regular Expression or regex
#string containing a combination of normal characters and special metacharacters that describe
#patters to find text or positions within a text


#r'st\d\s\w\{3,10}'
# Normal characters match themselves (st)
# metacharacters \d (digit)
# metacharacter \s (whitespace)
# metacharacter \w (word character) or ideas( between 3 and 10)

import re
#"re.findall(r"regex", string)"

test = re.findall(r"#movies", "Love #movies! I had fun yesterday going to the #movies")
print(test)

test2 = re.split(f"!", "Nice place to eat! i'll come back! Excelent meat")
print(test2)

#search an replace
test3 = re.sub(r"yellow", "nice", "I have a yellow car and yellow house in a yellow neighbordhood")
print(test3)

#search all the words with numbres
test4 = re.findall(r"User\d", "the winners are: User9, UserN, User8")
print(test4)

#search all the words with letter \d
test4 = re.findall(r"User\D", "the winners are: User9, UserN, User8")
print(test4)

#search all the words with any character \d
test4 = re.findall(r"User\w", "the winners are: User9, UserN, User8")
print(test4)

#search for $5
test = re.findall(r"\W\d", "this skirt is on sale, only $5 today!")
print(test)

#search for word with white space in the middle
test= re.findall(r"Data\sScience", "I enjoy learing Data Science")
print(test)

#replace for non-whitespace
test = re.sub(r"ice\Scream", "Ice Cream", "I really like ice-cream")
print(test)