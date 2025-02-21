import numpy as np
import os.path
from datetime import datetime
import yfinance as yf
import pandas as pd

end_date = datetime.now().strftime('%Y-%m-%d')
sharpe_threshold = 0.04
top_ten_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'JPM', 'BAC', 'WMT', 'V']
data_folder = './stock_data/'

# Ensure the data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Download data if not already downloaded
for ticker_symbol in top_ten_tickers:
    data_file = f"{data_folder}{ticker_symbol}.csv"

    if not os.path.exists(data_file):
        ticker_info = yf.Ticker(ticker_symbol)
        ticker_history = ticker_info.history(period="max")

        if not ticker_history.empty:
            ticker_history.to_csv(data_file)

# Analyze data
sharpe_ratios = []

for ticker_symbol in top_ten_tickers:
    data_file = f"{data_folder}{ticker_symbol}.csv"
    stock_data = pd.read_csv(data_file, index_col=0)

    if not stock_data.empty:
        stock_data['Daily_Return'] = stock_data['Close'].pct_change()
        risk_free_rate = 0.03
        daily_risk_free_rate = (1 + risk_free_rate) ** (1/252) - 1
        daily_returns = stock_data['Daily_Return']
        sharpe_ratio = np.mean(daily_returns - daily_risk_free_rate) / np.std(daily_returns)
        sharpe_ratios.append((ticker_symbol, sharpe_ratio))

# Sort and display the top ten tickers with the highest Sharpe ratios
sorted_sharpe_ratios = sorted(sharpe_ratios, key=lambda x: x[1], reverse=True)
for rank, (ticker, ratio) in enumerate(sorted_sharpe_ratios[:10], 1):
    print(f"Rank: {rank}")
    print(f"Ticker: {ticker}")
    print(f"Sharpe Ratio: {ratio}")
    print("---------------------")
