
from datetime import datetime

field1="sexiest job"
field2="data is produced daily"
field3="Individuals"
string1="httpswww.datacamp.com"
list_links=['www.news.com',
 'www.google.com',
 'www.yahoo.com',
 'www.bbc.com',
 'www.msn.com',
 'www.facebook.com',
 'www.news.google.com']



fact1=21
fact2=2500000000000000000
fact3=72.41415415151
fact4=1.111
number1=120
number2=7


# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")

# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

# Include both variables and the result of dividing them
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1 / number2:.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https','')}")


# Divide the length of list by 120 rounded to two decimals
print(f"Only {(len(list_links)*100/120):.2f}% of the posts contain links")

west=  {'date': datetime(2006, 5, 26, 0, 0), 'price': 1432673}

print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y.}")