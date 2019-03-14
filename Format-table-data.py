balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("\nName:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

print("\nName               Account         Charge     Balance")
for charge in open("balance_data.txt"):
    balance = balance - float(charge)
    print("{0:16}   {1:10}   {2:8,.2f}    {3:8,.2f}".format(name, account_no, float(charge), balance))
    #           2 decimales   2 decimales
