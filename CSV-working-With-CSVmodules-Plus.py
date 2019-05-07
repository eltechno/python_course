#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 3/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import csv
from datetime import datetime

path = "Google_Stock_ Market_Data - google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # first line is the head

data = [] #empty list
for row in reader:
    #row = [date, open, high, low, close, Volume, Adj. Close]
    # date = date time
    #open, high, low, close, adj close = float
    #volume = integer
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # 'open' is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date,open_price,high,low,close,volume,adj_close])


for i in range(len(data)):
    print(f'{i}: {data[i]}')

#compute and store daily stock returns
returns_path = "google_returns.csv"
file = open(returns_path, 'w') # w means writing mode
writer = csv.writer(file)
writer.writerow(["Date", "Return"]) #write the header into the file

for x in range(len(data) -1):
    today_row = data[x]
    todays_date = today_row[0]
    todays_price = today_row[-1]

    yesterday_row = data[x+1]
    yesterday_price = yesterday_row[-1]
    daily_return = ((todays_price - yesterday_price) / yesterday_price)
    #writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])

