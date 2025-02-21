import yfinance as yf
import csv
import time

companies = [
    'MMM', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AAP', 'AES', 'AFL', 'A', 
    'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 
    'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 
    'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'AOS', 'APA', 
    'AIV', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ANET', 'AJG', 'AIZ', 'ATO', 'T', 
    'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BAC', 'BK', 'BAX', 'BDX', 
    'BBY', 'BIIB', 'BLK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 
    'BR', 'CHRW', 'CDNS', 'CPB', 'COF', 'CPRI', 'CAH', 'KMX', 'CCL', 'CAT', 
    'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CF', 'SCHW', 'CHTR', 'CVX', 
    'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 
    'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 
    'STZ', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST', 'COTY', 'CCI', 'CSX', 'CMI', 
    'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'FANG', 
    'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DTE', 'DUK', 'DD', 'DXC', 
    'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EOG', 
    'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 
    'EXR', 'XOM', 'FFIV', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FISV', 
    'FLT', 'FLS', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 
    'GPS', 'GRMN', 'IT', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GL', 'GPN', 
    'GS', 'GWW', 'HRB', 'HAL', 'HBI', 'HOG', 'HIG', 'HAS', 'HCA', 'HP', 'HSIC', 
    'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HPQ', 'HUM', 
    'HBAN', 'HII', 'IEX', 'IDXX', 'ITW', 'ILMN', 'IR', 'INTC', 'ICE', 'IBM', 
    'INCY', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 
    'JKHY', 'J', 'JBHT', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KEY', 'KEYS', 
    'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 
    'LVS', 'LEG', 'LDOS', 'LEN', 'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 
    'LOW', 'LYB', 'MTB', 'M', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 
    'MA', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 
    'MSFT', 'MAA', 'MHK', 'TAP', 'MDLZ', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 
    'MSCI', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 
    'NKE', 'NI', 'JWN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 
    'NVR', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'PCAR', 'PKG', 'PH', 
    'PAYX', 'PYPL', 'PNR', 'PEP', 'PRGO', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 
    'PNC', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 
    'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'O', 'REG', 'REGN', 'RF', 
    'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 
    'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SLG', 
    'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SYF', 'SNPS', 
    'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'FTI', 'TFX', 'TXN', 
    'TXT', 'TMO', 'TJX', 'TSCO', 'TDG', 'TRV', 'TFC', 'TSN', 'UDR', 'ULTA', 
    'USB', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UHS', 'UNM', 'VFC', 
    'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'V', 'VNO', 'VMC', 'WRB', 'WAB', 
    'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WDC', 'WU', 'WRK', 
    'WY', 'WHR', 'WMB', 'WYNN', 'XEL', 'XRX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS'
]

def get_rsi(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    if hist.empty or 'Close' not in hist.columns:
        return None
    delta = hist['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

rsi_values = {}

for i, company in enumerate(companies):
    try:
        rsi = get_rsi(company)
        if rsi is not None:
            rsi_values[company] = rsi
        else:
            print(f"No data found for {company}")
    except Exception as e:
        print(f"Could not calculate RSI for {company}: {e}")
    time.sleep(1)  # To avoid hitting API rate limits
    print(f"Processed {i+1}/{len(companies)}")

sorted_rsi_values = sorted(rsi_values.items(), key=lambda item: item[1], reverse=True)

print("Companies ranked by RSI in descending order:")
for company, rsi in sorted_rsi_values:
    print(f"{company}: {rsi}")

with open('rsi_values.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company', 'RSI'])
    for company, rsi in sorted_rsi_values:
        writer.writerow([company, rsi])
