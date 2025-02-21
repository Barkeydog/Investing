import yfinance as yf
def get_top_companies():
    # Download S&P 500 data
    sp500 = yf.download('^GSPC', progress=False)
    sp500_tickers = sp500['Ticker'].tolist()
    # Create a dictionary to store market cap and P/E ratio of companies
    companies_data = {}

    # Fetch data for each company in the S&P 500
    for ticker in sp500_tickers:
        try:
            company = yf.Ticker(ticker)
            info = company.info
            if info.get('marketCap') is not None and info.get('forwardPE') is not None:
                market_cap = info['marketCap']
                forward_pe = info['forwardPE']
                companies_data[ticker] = {'MarketCap': market_cap, 'P/E': forward_pe}
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    # Sort companies based on market cap and P/E ratio
    sorted_by_market_cap = sorted(companies_data.items(), key=lambda x: x[1]['MarketCap'], reverse=True)
    sorted_by_pe_ratio = sorted(companies_data.items(), key=lambda x: x[1]['P/E'])

    return sorted_by_market_cap[:250], sorted_by_pe_ratio[:250]

# Get the top 250 companies based on market cap and P/E ratio
top_market_cap_companies, top_pe_ratio_companies = get_top_companies()

# Display the top 10 companies by market cap
print("Top 10 companies by Market Cap:")
for idx, (ticker, data) in enumerate(top_market_cap_companies[:10], start=1):
    print(f"{idx}. {ticker}: Market Cap - {data['MarketCap']:,}")

# Display the top 10 companies by P/E ratio
print("\nTop 10 companies by P/E ratio:")
for idx, (ticker, data) in enumerate(top_pe_ratio_companies[:10], start=1):
    print(f"{idx}. {ticker}: P/E Ratio - {data['P/E']:.2f}")
