import re

text = "Python 3 was released  on 12-03-2008"

information =re.search('(\d{1,2})-(\d{1,2})-(\d{4})', text)
# group 0 is the entire regex (\d{1,2})-(\d{1,2})-(\d{4})
# group 1 is the first part of the regex (\d{1,2})
# group 2 is the second part of the regex (again) (\d{1,2})
# group 3 is the third part of the regex  (\d{4})

print(information.group(3))
print(information.group(0))
# . group only can be used with .search or .match

#NAMING groups
text2 = "Austin, 78701"
cities = re.search(r"(?P<city>[A-Za-z]+).*?(?P<zipcode>\d{5})", text2)
print(cities.group("city"))
print(cities.group("zipcode"))

sentence = " i whish you a happy happy birthday"
#searching for the repetead word \1
print ( re.findall(r"(\w+)\s\1", sentence) )
#replace using the same regex
print ( re.sub(r"(\w+)\s\1", r"\1", sentence))

sentence2 = "your new code number is 23434. please, enter 23434 to open the door."
print ( re.findall(r"(?P<code>\d{5}).*?(?P=code)", sentence2))

#back reference a group name always use the \g
sentence3 = "this app is not working! It's repeating  the last word word"
print( re.sub(r"(?P<word>\w+)\s(?P=word)", r"\g<word>", sentence3))