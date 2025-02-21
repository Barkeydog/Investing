import yfinance as yf

# List of symbols for a diverse range of companies
company_symbols = [
    # Technology
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'INTC', 'IBM', 'ADBE',
    # ... (add more tech companies)

    # Healthcare
    'JNJ', 'PFE', 'MRK', 'ABT', 'MDT', 'TMO', 'GILD', 'AMGN', 'ABBV', 'BMY',
    # ... (add more healthcare companies)

    # Consumer Goods
    'PG', 'KO', 'PEP', 'NSRGY', 'UL', 'HD', 'MCD', 'NKE', 'COLM', 'KMB',
    # ... (add more consumer goods companies)

    # Energy
    'XOM', 'CVX', 'RDS-A', 'BP', 'TOT', 'COP', 'EOG', 'KMI', 'SLB', 'PSX',
    # ... (add more energy companies)

    # Real Estate
    'AMT', 'PLD', 'CCI', 'EQIX', 'SPG', 'PSA', 'WELL', 'AVB', 'EQR', 'PEAK',
    # ... (add more real estate companies)

    # Utilities
    'NEE', 'DUK', 'D', 'SO', 'AEP', 'EXC', 'SRE', 'XEL', 'PEG', 'WEC',
    # ... (add more utility companies)

    # Financial
    'JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'MA', 'AXP', 'USB', 'BLK',
    # ... (add more financial companies)

    # Industrials
    'MMM', 'BA', 'CAT', 'HON', 'UNP', 'GE', 'UPS', 'DE', 'EMR', 'FDX',
    # ... (add more industrial companies)

    # Transportation
    'TSLA', 'F', 'GM', 'NSC', 'CSX', 'DAL', 'AAL', 'UAL', 'LUV', 'ALK',
    # ... (add more transportation companies)

    # Services
    'AMZN', 'DIS', 'HD', 'CMCSA', 'VZ', 'NFLX', 'UPS', 'MCD', 'CRM', 'SBUX'
    # ... (add more service-related companies)
]

company_rankings = []

for symbol in company_symbols:
    company = yf.Ticker(symbol)
    info = company.info
    market_cap = info.get('marketCap', None)
    pe_ratio = info.get('trailingPE', None)

    if market_cap is not None and pe_ratio is not None:
        company_rankings.append({
            'symbol': symbol,
            'market_cap': market_cap,
            'pe_ratio': pe_ratio
        })

# Rank companies based on market capitalization
company_rankings.sort(key=lambda x: x['market_cap'], reverse=True)
for idx, company in enumerate(company_rankings):
    company['market_cap_rank'] = idx + 1

# Rank companies based on P/E ratio
company_rankings.sort(key=lambda x: x['pe_ratio'] if x['pe_ratio'] is not None else float('inf'))
for idx, company in enumerate(company_rankings):
    company['pe_ratio_rank'] = idx + 1

# Normalize ranks and calculate an overall score
max_rank = len(company_rankings)  # Maximum number of companies

for company in company_rankings:
    # Normalizing ranks between 0 and 1
    normalized_market_cap_rank = company['market_cap_rank'] / max_rank
    normalized_pe_ratio_rank = company['pe_ratio_rank'] / max_rank

    # Calculating an overall score between 1 and 100
    overall_score = ((normalized_market_cap_rank + normalized_pe_ratio_rank) / 2) * 100
    company['overall_score'] = overall_score

# Sort companies based on the overall score
company_rankings.sort(key=lambda x: x['overall_score'], reverse=True)
print("Overall Ranking with Scores (between 1 and 100):")
for idx, company in enumerate(company_rankings[:10]):
    print(f"{idx + 1}. {company['symbol']} - Overall Score: {company['overall_score']:.2f}")
