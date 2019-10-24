import requests
url ="http://www.omdbapi.com/?t=hackers&apikey=6b48d4b6"
#url ="http://www.omdbapi.com/?s=omen&apikey=6b48d4b6"
r = requests.get(url)
json_data =r.json()
for key, value in json_data.items():
    print(key +  ":", value)

