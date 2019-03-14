
name = input ("Please enter your name :")
livingLocation = input ("Please enter your living location :")
relationshipStatus = input ("Please enter your Relation Ship Status :")
employer = input ("Please enter your employer :")
jobTitle = input ("Please enter your Job Title :")
yearlyIncome = int(input ("Please enter your yearly income :"))

print ('{0:^16} | {1:<8}'.format("Nombre: ", name))
print ('{0:^16} | {1:<8}'.format("Location: ", livingLocation))
print ('{0:^16} | {1:<8}'.format("Status: ", relationshipStatus))
print ('{0:^16} | {1:<8}'.format("Employer: ", employer))
print ('{0:^16} | {1:<8}'.format("Job Title: ", jobTitle))
print ('{0:^16} | {1:<8}'.format("Yearly Income:  ", yearlyIncome*12))

