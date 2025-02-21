import investpy
import pandas as pd

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.B', 'JPM', 'JNJ', 'V',
           'PG', 'NVDA', 'DIS', 'MA', 'HD', 'PYPL', 'VZ', 'NFLX', 'ADBE', 'INTC']
pe_ratios = {}

for ticker in tickers:
    try:
        stock_data = investpy.get_stock_information(stock=ticker, country='United States')
        pe_ratio = stock_data['P/E'][0]
        if pe_ratio and pe_ratio != 'None':
            pe_ratios[ticker] = float(pe_ratio)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

pe_df = pd.DataFrame(list(pe_ratios.items()), columns=['Ticker', 'PE_Ratio'])
pe_df = pe_df.sort_values(by='PE_Ratio').reset_index(drop=True)

print(pe_df)

pe_df.to_csv('ranked_stocks_by_pe_ratio.csv', index=False)
