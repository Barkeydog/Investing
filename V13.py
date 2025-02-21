import yfinance as yf
import csv
import pandas as pd

companies = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'PYPL', 'ADBE', 'CSCO', 'INTC', 'CMCSA',
    'AVGO', 'TXN', 'QCOM', 'COST', 'TMUS', 'BKNG', 'GOOG', 'CHTR', 'SBUX', 'INTU', 'AMAT', 'ISRG', 'LRCX',
    'ADSK', 'VRSN', 'MRVL', 'KLAC', 'MNST', 'IDXX', 'MCHP', 'LULU', 'CDNS', 'SNPS', 'PAYX', 'CTSH', 'NXPI', 
    'FFIV', 'ANSS', 'VRSK', 'CPRT', 'DLTR', 'ROST', 'CTAS', 'REGN', 'BIIB', 'VRTX', 'ILMN', 'GILD', 'INCY', 
    'BMRN', 'AMGN', 'MRNA', 'BNTX', 'EXAS', 'CRSP', 'NTRS', 'SBAC', 'FANG', 'MELI', 'EBAY', 'BIDU', 'NTES', 
    'BABA', 'JD', 'PDD', 'BILI', 'DOCU', 'ZM', 'DDOG', 'CRWD', 'OKTA', 'TEAM', 'TWLO', 'PANW', 'NET', 'FSLY', 
    'ESTC', 'DRVN', 'ROKU', 'PTON', 'DASH', 'UBER', 'LYFT', 'ABNB', 'RBLX', 'ETSY', 'PINS', 'SNAP'
]

def get_atr(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    if hist.empty:
        return None
    high_low = hist['High'] - hist['Low']
    high_close = (hist['High'] - hist['Close'].shift()).abs()
    low_close = (hist['Low'] - hist['Close'].shift()).abs()
    tr = high_low.to_frame(name='TR')
    tr['High_Close'] = high_close
    tr['Low_Close'] = low_close
    tr = tr.max(axis=1)
    atr = tr.rolling(window=14).mean().iloc[-1]
    return atr

atr_values = {}

for company in companies:
    try:
        atr = get_atr(company)
        if atr is not None:
            atr_values[company] = atr
        else:
            print(f"No data found for {company}")
    except Exception as e:
        print(f"Could not calculate ATR for {company}: {e}")

sorted_atr_values = sorted(atr_values.items(), key=lambda item: item[1], reverse=True)

print("Companies ranked by ATR in descending order:")
for company, atr in sorted_atr_values:
    print(f"{company}: {atr}")

with open('atr_values.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company', 'ATR'])
    for company, atr in sorted_atr_values:
        writer.writerow([company, atr])
