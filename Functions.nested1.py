
def mod2plus5(x1, x2, x3):
    """returns the reminder plus 5 of three numbers"""

    def inner(x):
        """Returns the reminder plus 5 of a value"""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(1,2,3))

def raise_val(n):
    """Return the inner fuction"""

    def inner(x):
        """ Rise x to the power of n"""
        raised = x ** n
        return raised
    return inner

square = raise_val(3)
cube = raise_val(3)
print(square(2), cube(4))
