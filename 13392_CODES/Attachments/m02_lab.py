print("")
print("---- People --------------------------------------------------")

person_no = 1
with open('m02_lab_people','r') as people_file:

    for person in people_file:

        print(person_no, "    name:", person.strip())
        person_no += 1    # same as person_no = person_no + 1

print("")
print("total people: ", person_no-1)