
def add_all(*args):
    """Sum all values in *args together, args its a tuple"""

    #init sum
    sum_all= 0

    #accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

print(add_all(10,20,30,40))

