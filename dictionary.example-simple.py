
pop = [30.55, 2.77, 39.21]
countries = ["afganistan", "albania", "algeria"]

print(countries.index("albania"))# show what index (position have albania in the array

indice_alba = countries.index("albania") # assing the value of albania to a variable

print(indice_alba) #print the value

print(pop[indice_alba]) #print the value of albania index in the population array



# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
key = europe.keys()
print(key)

# Print out value that belongs to key 'norway'
print(europe["norway"])


world = {"afganistan": 30.55, "albania": 2.7, "algeria": 39.21}
print(world)

world["sealand"] = 0.000027 #adding a new value to the dictionary
print(world)

world["sealand"] = 0.000028 #modifiding the number
print(world)

print("sealand" in world) # check if the value exist

del(world["sealand"]) #deleting the new key and value
print(world)





# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']["capital"])

# Create sub-dictionary data
data = {"capital":"rome","population": 59.83}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)
