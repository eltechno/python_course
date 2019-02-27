
numbers = {
    items
    for items in range(2,471)
    if (items % 7 == 0)
    if (items % 5 != 0)
}

print (sorted(numbers))