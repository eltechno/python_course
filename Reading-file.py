
balance = 1000.00
name = "Chuck black"
accountNumber = "0112381321"

print ("Name: ", name, "   Account: ", accountNumber, "Original Balance: ", "$" + str(balance))
charges_file = open("balance_data.txt")

for charges in charges_file:
    balance = balance - float(charges) # cuando se lee de un archivo no sabe el programa que son numeros con decimales
    print("Name: ", name, "   Account: ", accountNumber, "charge: ", charges.strip(), "New Balance: ", "$"+ str(balance ))
