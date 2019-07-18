
my_string = "Where's Waldo"
print(my_string.find('Waldo'))

#when the string to find is not in place shows -1

print(my_string.find('Walda'))

#starting position and ending position
print(my_string.find('Waldo', 0,6))


print(my_string.index('Waldo'))

# when the string to find is not in place rise a exceptio
#print(my_string.index('Walda'))

#lets try with try-except block

try:
    my_string.index("wanda")
except ValueError:
    print("Not found")