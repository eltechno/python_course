from operator import itemgetter

from m05_03_functions_module_util import print_header
from m05_03_functions_module_util import read_charges
from m05_03_functions_module_util import print_charges_from_list
from m05_03_functions_module_util import print_charges_from_dict
from m05_03_functions_module_util import print_charges_with_default_param


# Initialize and print account information
bal = 1000.00
name = "Chuck Black"
acct_no = "01123581321"
print_header(name, acct_no, bal)

# Read, sort, and print charges
charges_list, charges_dict = read_charges("m00_charges-file")
charges_sorted_by_date = sorted(charges_list, key=itemgetter('date'))

print("\nUnsorted charges:")
bal = 1000.00
print_charges_from_list(charges_list, bal)
bal = 1000.00
print("\nSorted (by date) charges:")
print_charges_from_list(charges_sorted_by_date, bal)

print("\nSorted (by date) charges with default balance parameter:")
print_charges_with_default_param(charges_sorted_by_date)

bal = 1000.00
print("\nCharges from dictionary (random order but grouped by vendor)")
print_charges_from_dict(charges_dict, bal)

