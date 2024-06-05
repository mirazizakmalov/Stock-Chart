import pandas as pd 
import yfinance as yf
import datetime
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta

today = date.today()

ticker = input("What stock ticker would you like to look at: " )

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
data = yf.download(ticker, start = start_date, end = end_date, progress=False)

figure = px.line(data, x = data.index, y = "Close")
figure.update_layout(title = ticker + " Stock Price Analysis",  xaxis_rangeslider_visible=True)
print(data.head())
#figure.show()

#data = pd.read_csv("AAPL.csv")
#figure = go.Figure(go.Candlestick)
figure.show()