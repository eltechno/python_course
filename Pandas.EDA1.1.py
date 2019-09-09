import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', index_col=0)



print(iris)
print(iris.head)
iris.plot(x='petal_length', y='sepal_width')
plt.show()