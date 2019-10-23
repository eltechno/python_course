import  requests
url ="https://www.wikipedia.org/"
r = requests.get(url)
text = r.text
print(text)