import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', index_col=0)
print(iris.shape)

print(iris.head)
iris.plot(x='sepal_length', y='sepal_width')
plt.show()
#by default plot lines

iris.plot(x='sepal_lenght', y='sepal_width',
          kind='scatter')
plt.xlabel('sepal lenght (cm)')
plt.ylabel('sepal width (cm)')
plt.show()


iris.plot(y='sepal_leght', kind='box')
plt.ylabel('sepal width (cm)')
plt.show()

iris.plot(y='sepal_leght', kind='hist')
plt.ylabel('sepal width (cm)')
plt.show()

# bins (integer) number of intervals or bins
# range (tuple) extra of bins minimum and maximum
#normed (boolean) whether to normalize to one
#cumulative (boolean) compute Cumulative Distribution Fuction CDF


iris.plot(y='sepal_leght', kind='hist'
          bins=30, range(4,8), normaed=True)
plt.ylabel('sepal width (cm)')
plt.show()

iris.plot(y='sepal_leght', kind='hist'
          bins=30, range(4,8), cumulative=True, normed=True)
plt.ylabel('sepal width (cm)')
plt.title("Cumulative distribution fuction CDF")
plt.show()

#WARNING
#iris.plot(kind='hist')
#iris.plt.hist()
#iris.hist()
