import re

#re.search(r"regex", string)
#re.match(r"regex", string)

print(re.search(r"\d{4}", "4506 people attend the show"))
print(re.match(r"\d{4}", "4506 people attend the show"))


print(re.search(r"\d+", "Yesterday, I saw 3 shows"))
#this is because the first characters doesn't match the regex
print(re.match(r"\d+", "Yesterday, I saw 3 shows"))

#special characters (except newline) . (dot) match any character

my_links = "Just check out this link: www.amazingpics.com. it has amazing photos"
print(re.findall(r"www.+com", my_links))

my_string = "the 80s music was much better than the 90s"
print(re.findall(r"the\s\d+s", my_string))

#search only at the beggining ^
print(re.findall(r"^the\s\d+s", my_string))

#search only at last of the string $
print(re.findall(r"the\s\d+s$", my_string))

#split string at . (dot) and white space
my_string2="I love the music of Mr.Go. However, the sound was to loud"
print(re.split(r".\s", my_string2))
print(re.split(r"\.\s", my_string2)) #using the scape to work correctly

# OR operator
my_string3 = "Elephants  are the world's largest land animal! I would love to see an elephant one day"
print(re.findall(r"Elephant|elephant", my_string3))

my_string4 = "Yesterday I spent my afternoon with my friends: MaryJohn2 Clary3"
print(re.findall(r"[a-zA-Z]+\d", my_string4))