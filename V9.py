import pandas as pd
import numpy as np

# Read data from CSV file
data = pd.read_csv('zyxi.us [MConverter.eu].csv')  # Replace 'your_data.csv' with your file name

# Assuming your CSV columns are named 'CLOSE' for closing prices and 'DATE' for dates
daily_returns = data['CLOSE'].pct_change()
annualized_return = daily_returns.mean() * 252  # Assuming 252 trading days in a year

# Assuming risk-free rate is 0.03 (3%)
risk_free_rate = 0.03
annualized_volatility = daily_returns.std() * np.sqrt(252)

sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
print("Sharpe Ratio:", sharpe_ratio)
