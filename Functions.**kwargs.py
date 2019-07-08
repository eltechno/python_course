
def print_all(**kwargs):
    """Print out key-value pairs in **kwargs"""

    #print out the key-value pairs

    for key, value in kwargs.items():
        print(key + ":" + value)

print(print_all(name = "paulo", direccion = "guatemala"))