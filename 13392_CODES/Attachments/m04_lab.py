from operator import itemgetter

profiles_list = list()
profiles_dict = dict()

with open('m04_lab_profiles','r') as profiles_file:

    for profile_line in profiles_file:

        profile = dict()

        profile_info = profile_line.strip().split(',')

        profile['name'] = profile_info[0]
        profile['location'] = profile_info[1]
        profile['status'] = profile_info[2]
        profile['employer'] = profile_info[3]
        profile['job'] = profile_info[4]

        profiles_dict[profile_info[0]] = profile
        profiles_list.append(profile)


print("")
print("===================================== Unsorted Profiles ========================================================")
print("Name                  Location              Status        Employer                    Job")
print("--------------------  --------------------  -----------   ------------------------    --------------------------")

for profile in profiles_list:

    print("{:20}  {:20}  {:12}  {:26}  {:20}".format(profile['name'], profile['location'], profile['status'],
                                                     profile['employer'], profile['job']))

print("")
print("===================================== Sorted by Location ========================================================")
print("Name                  Location              Status        Employer                    Job")
print("--------------------  --------------------  -----------   ------------------------    --------------------------")

for profile in sorted(profiles_list, key=itemgetter('location')):

    print("{:20}  {:20}  {:12}  {:26}  {:20}".format(profile['name'], profile['location'], profile['status'],
                                                     profile['employer'], profile['job']))


print("")
print("===================================== Sorted by Employer =======================================================")
print("Name                  Location              Status        Employer                    Job")
print("--------------------  --------------------  -----------   ------------------------    --------------------------")

for profile in sorted(profiles_list, key=itemgetter('employer')):

    print("{:20}  {:20}  {:12}  {:26}  {:20}".format(profile['name'], profile['location'], profile['status'],
                                                     profile['employer'], profile['job']))


print("\n\n")
print("Name                  Location              Status        Employer                    Job")
print("--------------------  --------------------  -----------   ------------------------    --------------------------")
while True:

    name = input("Enter name: ")
    if len(name) == 0:
        break

    if name not in profiles_dict:
        print("I don't know anyone by the name of {}".format(name))
        continue

    profile = profiles_dict[name]
    print("{:20}  {:20}  {:12}  {:26}  {:20}".format(profile['name'], profile['location'], profile['status'],
                                                     profile['employer'], profile['job']))
