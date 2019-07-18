


custom_string = "String formatting"
print(f"{custom_string} is a powerfull technique")

tool = "Unsupervised algorithms"
goal = "patters"

print("{title} try to find {iam} in the database".format(title=tool, iam=goal))

#named place holders
my_method = {"tool": "Unsupervised algorithms", "goal": "patterns"}
print('{data[tool]} try to find {data[goal]} in the dataset'.format(data=my_method))

#float is the f
print("only {0:f}% of the {1} produced worldwide is {2}". format(0.5155675, "data", "analized"))

#float with 2 decimals
print("only {0:.2f}% of the {1} produced worldwide is {2}". format(0.5155675, "data", "analized"))

#data and time
from datetime import datetime
print(datetime.now())
print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))
