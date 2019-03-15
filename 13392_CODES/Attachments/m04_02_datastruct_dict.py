balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("name:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

charges_list = []
for charge_string in open("m00_charges-file"):
    charge_info_list = charge_string.strip().split(',')

    charge_info = dict()
    charge_info['vendor'] = charge_info_list[0]
    charge_info['date'] = charge_info_list[1]
    charge_info['charge'] = charge_info_list[2]

    charges_list.append(charge_info)

print("\n")
print("Vendor                     Date           Charge     Balance")
print("-----------------------    ----------    -------    --------")
for charge_info in charges_list:
    balance = balance - float(charge_info['charge'])
    print("{0:24}   {1:10}   {2:8,.2f}    {3:8,.2f}".format(charge_info['vendor'],
                                                            charge_info['date'],
                                                            float(charge_info['charge']),
                                                            balance))
