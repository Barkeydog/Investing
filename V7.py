import requests
import numpy as np

def get_data_from_github():
    github_json_url = 'https://github.com/rreichel3/US-Stock-Symbols/raw/main/nasdaq/nasdaq_full_tickers.json'

    try:
        response = requests.get(github_json_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Exception as e:
        return None

def calculate_sharpe_ratios(data):
    if data is None:
        return

    sharpe_ratios = []

    for entry in data:
        ticker_symbol = entry['symbol']
        daily_returns = np.random.rand(100)
        daily_risk_free_rate = 0.03 / 252

        sharpe_ratio = np.mean(daily_returns - daily_risk_free_rate) / np.std(daily_returns)
        sharpe_ratios.append((ticker_symbol, sharpe_ratio))

    sorted_sharpe_ratios = sorted(sharpe_ratios, key=lambda x: x[1], reverse=True)

    return sorted_sharpe_ratios

def display_top_ten(sorted_sharpe_ratios):
    if sorted_sharpe_ratios is None:
        return

    for rank, (ticker, ratio) in enumerate(sorted_sharpe_ratios[:10], 1):
        print(f"Rank: {rank}")
        print(f"Ticker: {ticker}")
        print(f"Sharpe Ratio: {ratio}")
        print("---------------------")

def run_daily_task():
    data = get_data_from_github()
    sorted_sharpe_ratios = calculate_sharpe_ratios(data)
    display_top_ten(sorted_sharpe_ratios)

run_daily_task()
