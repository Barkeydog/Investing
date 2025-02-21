import yfinance as yf
import csv

companies = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'PYPL',
    'ADBE', 'CSCO', 'INTC', 'CMCSA', 'AVGO', 'TXN', 'QCOM', 'COST', 'TMUS',
    'BKNG', 'GOOG', 'CHTR', 'SBUX', 'INTU', 'AMAT', 'ISRG', 'LRCX', 'ADSK',
    'VRSN', 'MRVL', 'KLAC', 'MNST', 'IDXX', 'MCHP', 'LULU', 'CDNS', 'SNPS',
    'PAYX', 'CTSH', 'XLNX', 'MXIM', 'SWKS', 'NXPI', 'FFIV', 'ANSS', 'VRSK',
    'CPRT', 'DLTR', 'ROST', 'CTAS', 'SGEN', 'REGN', 'BIIB', 'VRTX', 'ILMN',
    'GILD', 'ALXN', 'INCY', 'BMRN', 'AMGN', 'MRNA', 'BNTX', 'EXAS', 'CRSP',
    'NTRS', 'SBAC', 'FANG', 'MELI', 'EBAY', 'BIDU', 'NTES', 'BABA', 'JD',
    'PDD', 'BILI', 'DOCU', 'ZM', 'DDOG', 'CRWD', 'OKTA', 'TEAM', 'TWLO',
    'PANW', 'NET', 'FSLY', 'COUP', 'ESTC', 'DRVN', 'ROKU', 'PTON', 'DASH',
    'UBER', 'LYFT', 'ABNB', 'RBLX', 'ETSY', 'PINS', 'SNAP', 'TWTR', 'AAPL',
    'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'PYPL', 'ADBE',
    'CSCO', 'INTC', 'CMCSA', 'AVGO', 'TXN', 'QCOM', 'COST', 'TMUS', 'BKNG',
    'GOOG', 'CHTR', 'SBUX', 'INTU', 'AMAT', 'ISRG', 'LRCX', 'ADSK', 'VRSN',
    'MRVL', 'KLAC', 'MNST', 'IDXX', 'MCHP', 'LULU', 'CDNS', 'SNPS', 'PAYX',
    'CTSH', 'XLNX', 'MXIM', 'SWKS', 'NXPI', 'FFIV', 'ANSS', 'VRSK', 'CPRT',
    'DLTR', 'ROST', 'CTAS', 'SGEN', 'REGN', 'BIIB', 'VRTX', 'ILMN', 'GILD',
    'ALXN', 'INCY', 'BMRN', 'AMGN', 'MRNA', 'BNTX', 'EXAS', 'CRSP', 'NTRS',
    'SBAC', 'FANG', 'MELI', 'EBAY', 'BIDU', 'NTES', 'BABA', 'JD', 'PDD',
    'BILI', 'DOCU', 'ZM', 'DDOG', 'CRWD', 'OKTA', 'TEAM', 'TWLO', 'PANW',
    'NET', 'FSLY', 'COUP', 'ESTC', 'DRVN', 'ROKU', 'PTON', 'DASH', 'UBER',
    'LYFT', 'ABNB', 'RBLX', 'ETSY', 'PINS', 'SNAP', 'TWTR'
]


def get_pe_ratio(ticker):
  stock = yf.Ticker(ticker)
  pe_ratio = stock.info.get('trailingPE', None)
  return pe_ratio


pe_ratios = {}

for company in companies:
  pe_ratio = get_pe_ratio(company)
  if pe_ratio is not None:
    pe_ratios[company] = pe_ratio

sorted_pe_ratios = sorted(pe_ratios.items(), key=lambda item: item[1])

print("Companies ranked by P/E ratio in ascending order:")
for company, pe_ratio in sorted_pe_ratios:
  print(f"{company}: {pe_ratio}")

# Save the results to a CSV file
with open('pe_ratios.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Company', 'P/E Ratio'])
  for company, pe_ratio in sorted_pe_ratios:
    writer.writerow([company, pe_ratio])
