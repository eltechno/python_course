
total_seconds = 7385
hours = total_seconds// 3600 #truncate and division
remaining_seconds = total_seconds % 3600 # el residuo mod 3600
minutes = remaining_seconds //60  # divide 60 para encontrar segundos
seconds = remaining_seconds % 60 # mod segundos
print (hours, minutes, seconds)

#otro metodo
hours, remaining_seconds = divmod(total_seconds, 3600)
inutes, seconds = divmod(remaining_seconds, 60)
print (hours, minutes, seconds)

"""


/ --> Floating point division

// --> Floor division

Lets see some examples in both python 2.7 and in Python 3.5.

Python 2.7.10 vs. Python 3.5

print (2/3)  ----> 0                   Python 2.7
print (2/3)  ----> 0.6666666666666666  Python 3.5

Python 2.7.10 vs. Python 3.5

  print (4/2)  ----> 2         Python 2.7
  print (4/2)  ----> 2.0       Python 3.5

Now if you want to have (in python 2.7) same output as in python 3.5, you can do the following:

Python 2.7.10

from __future__ import division
print (2/3)  ----> 0.6666666666666666   #Python 2.7
print (4/2)  ----> 2.0                  #Python 2.7

Where as there is no differece between Floor division in both python 2.7 and in Python 3.5

138.93//3 ---> 46.0        #Python 2.7
138.93//3 ---> 46.0        #Python 3.5
4//3      ---> 1           #Python 2.7
4//3      ---> 1           #Python 3.5
"""