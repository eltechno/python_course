import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', index_col=0)
print(iris.shape)
print(iris.describe())
print(iris['sepal_width'].count())
print(iris['petal_length'].count())
print(iris['petal_width'].count())
print(iris['petal_length'].mean())
print(iris.mean())
print(iris.std())
print(iris.median())
q=[0.5, 0.75]
print(iris.quantile(q))
print(iris.min())
print(iris.max())