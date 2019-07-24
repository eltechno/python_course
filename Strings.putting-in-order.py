import pandas as pd
my_dataframe = pd.read_csv("wikipedia.csv", usecols=["description"])
#filter only the last description
wikipedia_article = my_dataframe.iloc[3,0]

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()
my_list = []
print(first_pos)
print(second_pos)

# Define string with placeholders
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

print(my_list)


# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))