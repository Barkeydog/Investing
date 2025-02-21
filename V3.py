import yfinance as yf

company_symbols = [
]

company_symbols = list(dict.fromkeys(company_symbols))

company_rankings = []

for industry_start_idx in range(0, len(company_symbols), count_per_industry):
    selected_companies = select_companies(industry_start_idx)
    for symbol in selected_companies:
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

company_rankings.sort(key=lambda x: x['market_cap'], reverse=True)
for idx, company in enumerate(company_rankings):
    company['market_cap_rank'] = idx + 1

company_rankings.sort(key=lambda x: float(x['pe_ratio']) if x['pe_ratio'] is not None else float('inf'))
for idx, company in enumerate(company_rankings):
    company['pe_ratio_rank'] = idx + 1

max_rank = len(company_rankings)

for company in company_rankings:
    normalized_market_cap_rank = company['market_cap_rank'] / max_rank
    normalized_pe_ratio_rank = company['pe_ratio_rank'] / max_rank

    overall_score = ((normalized_market_cap_rank + normalized_pe_ratio_rank) / 2) * 100
    company['overall_score'] = overall_score

company_rankings.sort(key=lambda x: x['overall_score'], reverse=True)
print("Overall Ranking with Scores (between 1 and 100):")
for idx, company in enumerate(company_rankings[:50]):
    print(f"{idx + 1}. {company['symbol']} - Overall Score: {company['overall_score']:.2f}")
