
import re
my_string = "I want to have a pet. But I don't know if i want a cat, a dog or a bird"
print(re.findall(r"cat|dog|bird", my_string))

my_string2 = "I want to have a pet. But I don't know if i want 2 cats, 1 dog or a bird"
print(re.findall(r"\d+\scat|dog|bird", my_string2 ))

#using grouping to get the correct answerd
print(re.findall(r"\d+\s(cat|dog|bird)", my_string2 ))

#now get all the info in tuple format
print(re.findall(r"(\d)+\s(cat|dog|bird)", my_string2 ))

#grouping but not capturing
my_string3 = "John Smith: 34-34-34-042-980, Rebeca: 10-10-10-434-425"
print(re.findall(r"(?:\d{2}-){3}(\d{3}-\d{3})", my_string3))

my_string4 = " Today is 23rd May 19. Tomorrow is 24th May 19"
print(re.findall(r"(\d+)(?:rd|th)", my_string4))
print(re.findall(r"(\w+\s\w+\s\d+)(?:rd|th)", my_string4))