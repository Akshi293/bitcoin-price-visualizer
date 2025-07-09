import requests
import pandas as pd
from datetime import datetime
import time
import os

def fetch_bitcoin_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '7',
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    dates = [datetime.fromtimestamp(item[0] / 1000.0).date() for item in prices]
    closing_prices = [item[1] for item in prices]

    df = pd.DataFrame({
        'Date': dates,
        'Close': closing_prices
    })

    # Calculate 3-day Simple Moving Average
    df['SMA_3'] = df['Close'].rolling(window=3).mean()

    return df

# --- MAIN LOOP ---
while True:
    df = fetch_bitcoin_data()
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal output
    print("📈 Real-Time Bitcoin Tracker (Last 7 Days)\n")
    print(df[['Date', 'Close', 'SMA_3']].to_string(index=False, formatters={
        'Close': '{:,.2f}'.format,
        'SMA_3': lambda x: '{:,.2f}'.format(x) if pd.notna(x) else 'N/A'
    }))
    
    print("\n🔁 Updating in 60 seconds...")
    time.sleep(60)
