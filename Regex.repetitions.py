import re
password = "password1234"

# with this we can specifi how many times the pattern exist
test=re.search(r"\w{8}\d{4}", password)
print(test)

# with the sign + means the character appear one or more times
text = "Date of start: 4-3. Date of registration: 10-04"
test = re.findall(r"\d+-\d+", text)
print(test)

#zero times or more:  *
my_string = "The concert was amazing! @ameli!a @john&&n @mary90"
test = re.findall(r"@\w+\W*\w+", my_string)
print (test)

#quantifiers zero times or once : ?
# in this example means the u will appear zero or once
text = " The color of this image is amazing. However, the colour blue could be brighter"
test = re.findall(r"colou?r", text)
print (test)

#quantifiers n times at least, m times at most {n, m}
phone_number = "John: 1-966-847-3131 Michele: 54-908-42-42424"
test = re.findall(r"\d{1,2}-\d{3}-\d{2,3}-\d{4}", phone_number)
print(test)