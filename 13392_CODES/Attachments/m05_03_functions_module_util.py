
def print_header(name, account_no, balance):

    print("name:", name, "    account:", account_no, "    original balance:", "$" + str(balance))


def read_charges(charges_file):

    charges = list()
    charges_dict = dict()

    for charge_string in open(charges_file):

        charge_info_list = charge_string.strip().split(',')

        charge_info = dict()
        charge_info['vendor'] = charge_info_list[0]
        charge_info['date'] = charge_info_list[1]
        charge_info['charge'] = charge_info_list[2]

        charges.append(charge_info)

        if charge_info['vendor'] not in charges_dict:
            charges_dict[charge_info['vendor']] = list()

        charges_dict[charge_info['vendor']].append(charge_info)

    return charges, charges_dict


def print_charge(vendor, date, charge, balance='n/a'):

    if type(balance) == float:
        print("{0:24}   {1:10}   {2:8,.2f}    {3:8,.2f}".format(vendor, date, charge, balance))
    else:
        print("{0:24}   {1:10}   {2:8,.2f}    {3:>8}".format(vendor, date, charge, balance))


def print_charges_from_dict(charges_dict, balance):

    print("Vendor                     Date           Charge     Balance")
    print("-----------------------    ----------    -------    --------")
    for vendor, charge_info_list in charges_dict.items():

        for charge_info in charge_info_list:

            balance = balance - float(charge_info['charge'])
            print_charge(charge_info['vendor'],charge_info['date'], float(charge_info['charge']), balance)


def print_charges_from_list(charges_list, balance):

    print("Vendor                     Date           Charge     Balance")
    print("-----------------------    ----------    -------    --------")
    for charge_info in charges_list:
        balance = balance - float(charge_info['charge'])
        print_charge(charge=float(charge_info['charge']),
                     date=charge_info['date'],
                     balance=balance,
                     vendor=charge_info['vendor'])


def print_charges_with_default_param(charges_list):

    print("Vendor                     Date           Charge     Balance")
    print("-----------------------    ----------    -------    --------")
    for charge_info in charges_list:
        print_charge(charge=float(charge_info['charge']),
                     date=charge_info['date'],
                     vendor=charge_info['vendor'])


