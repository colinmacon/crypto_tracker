import shrimpy
import pandas as pd
import talib as ta
import numpy as np
import plotly.graph_objects as go
from config import *


class Track:

    def __init__(self):
        # create the client
        self.client = shrimpy.ShrimpyApiClient(public_key, secret_key)

    def setup(self, crypto_symbol, time_interval):
        self.crypto_symbol = crypto_symbol
        self.time_interval = time_interval

    #Getting the base data
    def get_data(self):
        # get the candles
        candles = self.client.get_candles(
            'bittrex',  # exchange
            self.crypto_symbol,      # base_trading_symbol
            'USDT',      # quote_trading_symbol
            self.time_interval       # interval 1m, 5m, 15m, 1h, 6h, or 1d
        )

        # create lists to hold our different data elements
        dates = []
        open_data = []
        high_data = []
        low_data = []
        close_data = []

        # convert from the Shrimpy candlesticks to the plotly graph objects format
        for candle in candles:
            dates.append(candle['time'])
            open_data.append(candle['open'])
            high_data.append(candle['high'])
            low_data.append(candle['low'])
            close_data.append(candle['close'])

        self.df = pd.DataFrame({'dates': dates, 'open_data': open_data, 'high_data': high_data,
                           'low_data': low_data, 'close_data': close_data})

        #Convrting df to floats
        self.df = self.df.apply(pd.to_numeric, errors='ignore')

    #Expanding the df with some simple indicators to track
    def expand_df(self):
        #Getting the EMA lines 50/200
        self.df['EMA50'] = ta.EMA(self.df['close_data'], timeperiod=50)
        self.df['EMA200'] = ta.EMA(self.df['close_data'], timeperiod=200)

        #Putting in an uptrend or downtrend column as well
        self.df['trend'] = np.where(self.df['EMA50'] > self.df['EMA200'], 'uptrend', 'downtrend')


    #Generating a report
    def report(self):
        #Getting everything were going to need for the report
        last_price = self.df.close_data.iloc[-1]
        last_trend = self.df.trend.iloc[-1]
        price_change = self.df.close_data.iloc[-1] - self.df.open_data.iloc[-1]

        price_message = f"Last price was: {round(last_price,3)}"
        trend_message = f"The current trend is: {last_trend}"
        pc_message = f"The price change today was: {round(price_change,2)}"

        print(f"{self.crypto_symbol} stats are the following:\n")
        print(price_message,trend_message,pc_message,sep='\n')

    #Plotting the close candles and EMAs now
    def create_plot(self):
        fig = go.Figure(data=[go.Candlestick(x=self.df['dates'],
                       open=self.df['open_data'], high=self.df['high_data'],
                       low=self.df['low_data'], close=self.df['close_data']),
                       go.Scatter(x=self.df.dates, y=self.df.EMA50, line=dict(color='sienna', width=1)),
                      go.Scatter(x=self.df.dates, y=self.df.EMA200, line=dict(color='blue', width=1))])

        fig.show()
