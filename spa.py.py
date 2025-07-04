import yfinance as yf
import pandas as pd
import datetime as dt
import numpy as np


endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*5)

stocks = ['MSFT','NVDA' ,'NTDOY' ,'AAPL']

df = yf.download(stocks, start = startDate, end = endDate, auto_adjust=True)


close_Prices = df['Close']

print (close_Prices.head())