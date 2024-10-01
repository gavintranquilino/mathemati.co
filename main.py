import yfinance as yf
import matplotlib.pyplot as plt

STOCK_TICKER = "tsla"  # customizable

# init a ticker class and specify the stock ticker/symbol & call history method
STOCK = yf.Ticker(STOCK_TICKER)
STOCK_HISTORY = STOCK.history(period="max")  # has useful methods like to_csv()

del STOCK_HISTORY['Dividends']  # remove dividends column
del STOCK_HISTORY['Stock Splits']  # remove stock splits column


STOCK_HISTORY.plot.line(y='Close', title=f'{STOCK_TICKER} Stock Price', use_index=True)  # plot the closing price of the stock vs time



plt.show()  # display all the graphs
