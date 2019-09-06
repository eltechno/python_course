import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


appl = pd.read_csv('aapl.csv', index_col='date', parse_dates=True)
close_series = appl['close']
print(type(close_series))

plt.plot(close_series)
plt.show()

#we can use the same plot as the same
close_series.plot() #plots series directly
plt.show()


appl.plot() # plot all series all the same time
plt.show()

#fixiing scale
appl.plot()
plt.yscale('log') #locarithmic scale on vertical axis
plt.show()

appl['open'].plot(color='b', style='.-', legend=True)
appl['close'].plot(color='r', style='.', legend=True)

plt.axis(('2001', '2002', 0,100))
plt.show()


appl.loc['2001':'2004', ['open', 'close', 'high', 'low']].plot()
#plt.savefig('appl.png')
#plt.savefig('appl.jpg')
#plt.savefig('appl.pdf')
plt.show()