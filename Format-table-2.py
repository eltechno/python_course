# if you want to get everything in column 3
col_num = 2
col_data = []
delimiter = " "
with open('people-list.txt') as f:
    col_data.append(f.readline().split(delimiter))
print (col_data)
