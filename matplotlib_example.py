#!/usr/bin/python3

#############################################################################
#                                 Matplotlib                                #
#############################################################################
#
# Prequisites:
# apt-get install libjpeg-dev zlib1g-dev
# pip3 install --upgrade pip
# pip3 install --upgrade setuptools
# pip3 install --upgrade pillow
# pip3 install --upgrade matplotlib


import pdb
import csv
import numpy as np
import matplotlib.pyplot as plt


# EXAMPLE 1 - simple data to file  
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
  
plt.plot(Year, Unemployment_Rate)
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.savefig('unemployment.png')


# EXAMPLE 2 - show data from csv
# clearing the plot
plt.clf()

time = []
bid = []
ask = []
# opening the CSV file
with open('input.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # extracting the contents of the CSV file (Time,Bid,Ask), 3 comma separated fields
  for lines in csvFile:
        if 'Time' in lines and 'Bid' in lines and 'Ask' in lines:
            continue
        time.append(lines[0])
        bid.append(float(lines[1]))
        ask.append(float(lines[2]))

plt.title("BidAsk over time")
plt.xlabel("time")
plt.xlabel("price")
plt.plot(time, bid, color="red")
plt.plot(time, ask, color="blue")

# Limit the ticks on the x axis
xticks = [time[0], time[int(len(time)/2)], time[-1]]
plt.xticks(xticks)
yticks = [0, min(bid), max(max(bid[1:-1]), max(ask[1:-1]))*2]
plt.yticks(yticks)
plt.show()
