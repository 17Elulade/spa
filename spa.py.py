import yfinance as yf
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
#Libraries used in this project


endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*5)

#The datetime function allows us to specifically select a period of time

stocks = ['MSFT','NVDA' ,'NTDOY' ,'AAPL']
df = yf.download(stocks, start = startDate, end = endDate, auto_adjust=True)

#Created a list of stocks I am using, and used yfinance to doownload their details and assigned it to a dataframe

close_Prices = df['Close']
log_DReturns = np.log(close_Prices/close_Prices.shift(1))

#made a seperate dateframe for their close prices

#divided the prices from the day before and found the log of that value 
#first row divded by nothing thats why it's not accessible

log_CumuReturns = log_DReturns.cumsum()

#Each day takes the previous value, adds it to the next day and stores it,
# cycles thorugh add the next value and will either increase or drcease over time 

log_CumuReturns.plot(title = 'Cumulative Returns',figsize = (10,6))

plt.show()
