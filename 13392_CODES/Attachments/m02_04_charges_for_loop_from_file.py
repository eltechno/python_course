balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("name:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

charges_file = open("m00_charges-only-file")
for charge in charges_file:
    balance = balance - float(charge)
    print("name:", name, "    account:", account_no, "    charge:", charge.strip(), "    new balance:", "$" + str(balance))
