# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value), end="\n\n")

# Loop over range(3) and print the values
for i in range(3):
    print(i, end="\n\n")


# Create an iterator for range(10 ** 100): googol
googol = iter( range(10 ** 100))

#The value 10^100 is actually what's called a Googol which is a 1 followed by a hundred 0s

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))