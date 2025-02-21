import yfinance as yf
import numpy as np
from datetime import datetime

end_date = datetime.now().strftime('%Y-%m-%d')
sharpe_threshold = 0.05
top_ten_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'JPM', 'BAC', 'WMT', 'V']

for ticker_symbol in top_ten_tickers:
    ticker_info = yf.Ticker(ticker_symbol)
    ticker_history = ticker_info.history(period="max")
    if not ticker_history.empty:
        start_date = ticker_history.index[0].strftime('%Y-%m-%d')
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        if not stock_data['Close'].empty:
            stock_data['Daily_Return'] = stock_data['Close'].pct_change()
            risk_free_rate = 0.03
            daily_risk_free_rate = (1 + risk_free_rate) ** (1/252) - 1
            daily_returns = stock_data['Daily_Return']
            sharpe_ratio = np.mean(daily_returns - daily_risk_free_rate) / np.std(daily_returns)
            if sharpe_ratio > sharpe_threshold:
                action = 'Buy'
            else:
                action = 'Sell'
            print(f"Ticker: {ticker_symbol}")
            print(f"Start Date: {start_date}")
            print(f"Sharpe Ratio: {sharpe_ratio}")
            print(f"Action: {action}")
            print("---------------------")
        else:
            print(f"Close data is empty for {ticker_symbol}. Skipping...")
    else:
        print(f"No historical data available for {ticker_symbol}. Skipping...")
