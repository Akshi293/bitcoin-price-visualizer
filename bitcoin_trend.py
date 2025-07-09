import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

plt.ion()  # Turn on interactive mode

def fetch_and_plot():
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

    df['SMA_3'] = df['Close'].rolling(window=3).mean()

    # Clear previous plot
    plt.clf()
    plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='gold', label='Closing Price')
    plt.plot(df['Date'], df['SMA_3'], linestyle='--', color='blue', label='3-Day SMA')
    plt.title("Real-Time Bitcoin Price (Updated Every 60 Secs)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

    return df

# Loop every 60 seconds
while True:
    fetch_and_plot()
    time.sleep(60)
