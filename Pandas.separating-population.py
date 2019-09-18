import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


iris = pd.read_csv("iris.csv")

print(iris["species"].describe())
print(iris["species"].unique())

indices = iris['species'] == 'setosa'

setosa = iris.loc[indices,:] #create a new DATAFRAME
setosa.plot(kind="hist", bins=50, range=(0,8), alpha=0.3)
#graph the dataframe
plt.title("Setosa data set")
plt.xlabel("[cm]")

indices = iris['species'] == 'versicolor'
versicolor = iris.loc[indices,:] #create a new DATAFRAME
#graph the dataframe
versicolor.plot(kind="hist", bins=50, range=(0,8), alpha=0.3)
plt.title("Versicolor data set")
plt.xlabel("[cm]")


indices = iris['species'] == 'virginica'
virginica = iris.loc[indices,:] #create a new DATAFRAME
#graph the dataframe
virginica.plot(kind="hist", bins=50, range=(0,8), alpha=0.3)
plt.title("Virginica data set")
plt.xlabel("[cm]")


print(setosa)
print(versicolor)
print(virginica)

#checking species
setosa['species'].unique()
versicolor['species'].unique()
virginica['species'].unique()

del setosa['species'], versicolor['species'], virginica['species']

#checking indexes
print(setosa.head(2))

print(versicolor.head(2))
print(virginica.head(2))

iris.plot(kind="hist", bins=50, range=(0,8), alpha=0.3)
plt.title("Entire iris data set")
plt.xlabel("[cm]")
#plt.show()

describe_all= iris.describe()
print(describe_all)

describe_setosa = setosa.describe()
describe_versicolor = versicolor.describe()
describe_viginica = virginica.describe()

#computing errors
error_setosa = 100 * np.abs(describe_setosa - describe_all)
error_setosa = error_setosa / describe_setosa
print("this is the error setora")
print(error_setosa)

#computing errors
error_versicolor = 100 * np.abs(describe_versicolor - describe_all)
error_versicolor = error_versicolor / describe_versicolor
print("this is the error versicolor")
print(error_versicolor)

#computing errors
error_virginica = 100 * np.abs(describe_viginica - describe_all)
error_virginica = error_virginica / describe_viginica
print("this is the error virginica")
print(error_virginica)

