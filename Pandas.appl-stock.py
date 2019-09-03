import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


appl = pd.read_csv('aapl.csv', index_col='date', parse_dates=True)

print(appl.head(6))

close_arr = appl['close'].values
print(type(close_arr))

plt.plot(close_arr)
plt.show()