from operator import itemgetter
from datetime import date
import calendar


def get_date(date_string):

    year = int(date_string[:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])

    if month not in range(1,13) or day not in range(1,32):
        return date(1969,1,1)

    return date(year, month, day)


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


def write_charges_to_file(charges_list, balance, output_filename):

    if len(charges_list) == 0: return balance

    with open(output_filename, 'w') as out:
        out.write("Vendor                     Year  Month      Day    Charge     Balance\n")
        out.write("-----------------------    ----  ---------  ---    -------    --------\n")
        for charge_info in charges_list:
            balance = balance - float(charge_info['charge'])
            charge_date = get_date(charge_info['date'])
            out.write("{:24}   {:4}  {:9}  {:3}  {:8,.2f}    {:8,.2f}\n".format(charge_info['vendor'],
                                                                                charge_date.year,
                                                                                calendar.month_name[charge_date.month],
                                                                                charge_date.day,
                                                                                float(charge_info['charge']),
                                                                                balance))

    return balance


#-----------------------------------------------------------------------------

# Read charges
charges_list, charges_dict = read_charges("m06_charges-file")

bal = new_bal = 1000.00
sorted_charges = sorted(charges_list, key=itemgetter('date'))

current_year = 0
for charge in sorted_charges:

    this_year = get_date(charge['date']).year
    if this_year != current_year:

        if current_year != 0:
            new_bal = write_charges_to_file(charges_by_year, bal, "m06_charges-out-"+str(current_year))

        charges_by_year = list()
        current_year = this_year
        bal = new_bal

    charges_by_year.append(charge)

write_charges_to_file(charges_by_year, bal, "m06_charges-out-"+str(current_year))