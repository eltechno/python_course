

addressBook = []
#for items in open("people-list.txt"):
#        addressBook.append(items.strip())
#print (addressBook)

source = open('people-list.txt')
#for line in source:
#    fields = line.split('\t')
#    addressBook.append(fields)

#for line in addressBook:
#   print ("\t".join(line))

changes_files = open('charges_file.txt')
for charges_info_string in changes_files:
    charges_info = charges_info_string.strip().split(',')
    print(charges_info)

