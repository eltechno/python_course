print("")
print("---- People --------------------------------------------------")

person_no = 1
with open('people-list.txt','r') as people_file:

    for person in people_file:

        print(person_no, "    name:", person.strip())
        person_no += 1    # same as person_no = person_no + 1

print("")
print("total people: ", person_no-1) o separadas
