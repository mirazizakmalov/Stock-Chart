import pandas as pd 
import yfinance as yf
import datetime
from datetime import date, timedelta

import plotly.express as px
import plotly.graph_objects as go


#Variables
ticker = input("What stock ticker would you like to look at: " )
choice = input("What would you like to see?")
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
data = yf.download(ticker, start = start_date, end = end_date, progress=False)

print(data)
 
# #Table
# print(data.head())

# #Line Graph
# figure = px.line(data, x = data.index, y = "Close")
# figure.update_layout(title = ticker + " Stock Price Analysis",  xaxis_rangeslider_visible=True)
# figure.show()

#CandleStick Graph
figure = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data["Open"],
    high=data["High"],
    low=data["Low"],
    close=data["Close"]
)])

figure.update_layout(
    title=f"{ticker} Stock Price Analysis",
    xaxis_rangeslider_visible=False
)

figure.show()

