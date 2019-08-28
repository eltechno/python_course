
with open("world_ind_pop_data.csv") as file:
    file.readline()
    count_dict = {}
    for j in range(1000):
        line = file.readline().split(',')
        first_col = line[0]

        if first_col in count_dict.keys():
            count_dict[first_col] +=1
        else:
            count_dict[first_col] = 1

print(count_dict)