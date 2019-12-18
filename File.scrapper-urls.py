from urllib.request import urlopen, Request

url="https://www.wikipedia.org/"
request = Request(url)
response =urlopen(request)
html = response.read()
print(html)
response.close()