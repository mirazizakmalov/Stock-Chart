import pandas as pd 
import yfinance as yf
from datetime import date, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Variables
ticker = input("What stock ticker would you like to look at: ")
print("0: Print a table")
print("1: Display a line graph")
print("2: Display a candlestick graph with volume")
choice = int(input("What would you like to see? "))  # Convert input to int

today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

# Downloading data
data = yf.download(ticker, start=start_date, end=end_date, progress=False)

def switch(argument):
    if argument == 0:
        # Print table
        print(data.head())
        
    elif argument == 1:
        # Line Graph
        figure = px.line(data, x=data.index, y="Close")
        figure.update_layout(title=f"{ticker} Stock Price Analysis", xaxis_rangeslider_visible=True)
        figure.show()
        
    elif argument == 2:
        # Candlestick Graph with Volume
        figure = make_subplots(rows=2, cols=1, shared_xaxes=True,
                               row_heights=[0.7, 0.3],  # Adjust heights as needed
                               vertical_spacing=0.02)

        candlestick = go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name='Candlestick'
        )

        volume = go.Bar(
            x=data.index,
            y=data['Volume'],
            name='Volume',
            marker_color='blue'
        )

        figure.add_trace(candlestick, row=1, col=1)
        figure.add_trace(volume, row=2, col=1)

        figure.update_layout(
            #The f before the string in f"{ticker} Stock Price and Volume Analysis" is used to create an f-string, which is a way to format strings in Python
            title=f"{ticker} Stock Price and Volume Analysis",
            xaxis_rangeslider_visible=True,
            yaxis_title='Stock Price',
            yaxis2_title='Volume',
            legend=dict(
                orientation='h',
                x=0.5,
                xanchor='center',
                y=1.1,
                yanchor='top'
            )
        )
        figure.show()
        
    else:
        print("Invalid choice")

# Call the switch function with the user's choice
switch(choice)

