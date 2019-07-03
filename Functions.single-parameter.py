
def square(value):
    new_value = value ** 2
    print(new_value)


square(10)
square(5)

#but now we dont want to print the value instead will return
#in order to be a assignable value

def square2(value):
    """ Return the square of a value"""
    new_value = value ** 2
    return new_value

num =square2(10)
print("this is the assignable value", num)


# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout("congratulations")