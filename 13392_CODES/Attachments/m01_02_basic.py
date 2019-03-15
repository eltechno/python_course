balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("name:", name, "    account:", account_no, "    balance:", balance)
print("name:", name, "    account:", account_no, "    balance:", "$" + str(balance))
print("name:", name, "    account:", account_no, "    balance:", "$" + str(float(balance)))

print("\n")

balance = 1000.00
new_balance = balance
balance += 250
                                #show the ID of the object id()
print("balance object id:    ", id(balance),     "    balance value:    ", balance)
print("new balance object id:", id(new_balance), "    new balance value:", new_balance)