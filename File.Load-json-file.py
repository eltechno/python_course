
#load json : json_data

import json

with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

for key, value in json_data.items():
    print(key, ":", value)


# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])