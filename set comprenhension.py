
names = {"arkadiusz", "Agness", "carol", "james", "Eric", "Susane"}

namesCapitalized  = [
    items.capitalize()
    for items in names
]

namesCapitalized2 = {
    items
    for items in namesCapitalized
    if items.startswith("A")
}

print (namesCapitalized)
print (namesCapitalized2)