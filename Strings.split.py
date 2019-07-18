
my_string = "This string will be split"
my_string2 = "This string will be split"

"""
Parameter 	Description
separator 	Optional. Specifies the separator to use when splitting the string. Default value is a whitespace
max 	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

"""
print(my_string.split(sep=" ", maxsplit= 2))

print(my_string2.rsplit(sep=" ", maxsplit= 2))

my_string3= "This string will be split \nin two parts"

print(my_string3.splitlines())

my_list = ["this", "would", "be", "a", "string"]

print(" ".join(my_list))





file = 'mtv films election, a high school comedy, is a current example\nfrom there, director steven spielberg wastes no time, taking us into the water on a midnight swim'

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(",")
    print(substring_split)
