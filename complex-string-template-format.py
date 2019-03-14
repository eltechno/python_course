id = "IAD"
location = "dulles Intl Airport"
max_temp = 32
min_temp = 13
precipitation = 0.4

#'(IAD) : (Dulles Intl Airport) : (32) / (13) / (0.4)'

print("First Method")
print ('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format(
      id=id, location=location, max_temp=max_temp,
     min_temp=min_temp, precipitation=precipitation))
print("")

print("Second Method")
data=dict(id=id, location=location, max_temp=max_temp,min_temp=min_temp, precipitation=precipitation)
print ('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(data))
print("")

print("third method, the most simple")
print ('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars()))

"""
b for binary
c for Unicode Character
d is for decimal numbers
e and e are for scientific niotations
f and f are for floating-point
g and g are for general
n is for locale-specific decimal numbers
o for octal, base8
s is for string
X and x for hexadecimal base 16
% is for percentage
"""
