import pandas as pd

data = {"weekday": ['sun', 'sun', 'mon', 'mon'],
        'city': ['Austin', 'Dallas', 'Austing', 'Dallas'],
        'visitors': [139,237,326,456],
        'signups': [7,12,3,5]}

users = pd.DataFrame(data)
print(users)


cities = ['Austin', 'Dallas', 'Austing', 'Dallas']
weekday  =['sun', 'sun', 'mon', 'mon']
city= ['Austin', 'Dallas', 'Austing', 'Dallas']
visitors = [139,237,326,456]
signups = [7,12,3,5]
list_labels = ["city", "signups", "visitors", "weekday"]
list_cols = [cities, signups, visitors, weekday]
zipped = list(zip(list_labels, list_cols))

data2 = dict(zipped)
users2 = pd.DataFrame(data2)
users2['fees'] = 0 # broadcasting
print(users2)