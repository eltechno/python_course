courses = ['artificial intelligence', 'neural networks']

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Define string with placeholders
my_message = "If you are interested in {plan[field]}, you can take the course related to {plan[tool]}"

# Use dictionary to replace placehoders
print(my_message.format(plan=plan))