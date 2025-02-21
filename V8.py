import pandas as pd
import numpy as np

file_path = 'aapl.us.txt'  # 
data = pd.read_csv(file_path, header=None)
data.columns = ['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL', 'OPENINT']

data['DATETIME'] = pd.to_datetime(data['DATE'].astype(str) + data['TIME'].astype(str), format='%Y%m%d%H%M%S')

data['RETURNS'] = data.groupby('DATE')['CLOSE'].pct_change()

daily_mean_return = data['RETURNS'].mean()
daily_std_return = data['RETURNS'].std()
risk_free_rate = 0.03  

sharpe_ratio = (daily_mean_return - risk_free_rate) / daily_std_return
annual_sharpe_ratio = sharpe_ratio * np.sqrt(252) 

print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
print(f"Annualized Sharpe Ratio: {annual_sharpe_ratio:.4f}")
