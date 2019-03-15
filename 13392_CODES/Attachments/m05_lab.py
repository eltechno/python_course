from operator import itemgetter

def read_profiles(filename):

    profiles_list = list()
    profiles_dict = dict()

    with open(filename,'r') as profiles_file:

        for profile_line in profiles_file:

            profile = dict()

            profile_info = profile_line.strip().split(',')

            profile['name'] = profile_info[0]
            profile['location'] = profile_info[1]
            profile['status'] = profile_info[2]
            profile['employer'] = profile_info[3]
            profile['job'] = profile_info[4]

            profiles_dict[profile_info[0].lower()] = profile
            profiles_list.append(profile)

    return profiles_list, profiles_dict


def print_profiles(profiles_list):

    print("Name                  Location              Status        Employer                    Job")
    print("--------------------  --------------------  -----------   ------------------------    --------------------------")
    for profile in profiles_list:
        print("{:20}  {:20}  {:12}  {:26}  {:20}".format(profile['name'], profile['location'], profile['status'],
                                                         profile['employer'], profile['job']))


def find_and_print_profile(entered_name, dictionary_of_profiles):

    normalized_name = entered_name.lower().strip()
    if normalized_name not in dictionary_of_profiles:
        print("I don't know anyone by the name of {}".format(entered_name))
    else:
        profile = dictionary_of_profiles[normalized_name]
        print("\n  Result:     name : ", profile['name'])
        print(  "          location : ", profile['location'])
        print(  "            status : ", profile['status'])
        print(  "          employer : ", profile['employer'])
        print(  "               job : ", profile['job'])


#-----------------------------------------------------------------------------

profiles_list, profiles_dict = read_profiles("m04_lab_profiles")

print("\n=============================== Unsorted Profiles =======================================================")
print_profiles(profiles_list)

print("\n============================== Sorted by Location =======================================================")
print_profiles(sorted(profiles_list, key=itemgetter('location')))

print("\n============================== Sorted by Employer =======================================================")
print_profiles(sorted(profiles_list, key=itemgetter('employer')))

print("\n========================== Search by Profile Name =====================================================\n")
while True:

    name = input("\nEnter name:  ")
    if len(name) == 0: break

    find_and_print_profile(dictionary_of_profiles=profiles_dict, entered_name=name )


