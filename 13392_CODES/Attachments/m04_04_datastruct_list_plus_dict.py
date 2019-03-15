from operator import itemgetter

balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("name:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

charges_list = list()
charges_dict = dict()
for charge_string in open("m00_charges-file"):
    charge_info_list = charge_string.strip().split(',')

    charge_info = dict()
    charge_info['vendor'] = charge_info_list[0]
    charge_info['date'] = charge_info_list[1]
    charge_info['charge'] = charge_info_list[2]

    charges_list.append(charge_info)

    if charge_info['vendor'] not in charges_dict:
        charges_dict[charge_info['vendor']] = list()

    charges_dict[charge_info['vendor']].append(charge_info)

charges_sorted_by_date = sorted(charges_list, key=itemgetter('date'))

print("\n")
print("Vendor                     Date           Charge     Balance")
print("-----------------------    ----------    -------    --------")
balance = 1000.00
for charge_info in charges_sorted_by_date:
    balance = balance - float(charge_info['charge'])
    print("{0:24}   {1:10}   {2:8,.2f}    {3:8,.2f}".format(charge_info['vendor'],
                                                            charge_info['date'],
                                                            float(charge_info['charge']),
                                                            balance))

print("\n")
print("Vendor                     Date           Charge     Balance")
print("-----------------------    ----------    -------    --------")
balance = 1000.00
for vendor, charge_info_list in charges_dict.items():

    for charge_info in charge_info_list:

        balance = balance - float(charge_info['charge'])
        print("{0:24}   {1:10}   {2:8,.2f}    {3:8,.2f}".format(charge_info['vendor'],
                                                                charge_info['date'],
                                                                float(charge_info['charge']),
                                                                balance))

    print("--")



