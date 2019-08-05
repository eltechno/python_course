import re

string = " Clary has 2 friends, who she spend a lot time with. Susan has 3 brothers while John has 4 sisters"

print (re.findall('[A-Za-z]+\s\w+\s\d+\s\w+', string))

print (re.findall('([A-Za-z]+)\s\w+\s\d+\s\w+', string))

print (re.findall('([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', string))

#organize the data

pets = re.findall('([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', "Clary has 2 dogs but John has 3 cats")
print(pets[0][0])
