# 🪙 Bitcoin Price Visualizer

A beginner-friendly Python project that fetches and visualizes real-time Bitcoin prices using the CoinGecko API. It includes both a terminal-based tracker and a graphical visualization with a 3-day Simple Moving Average (SMA).

---

## 📈 Features

- 🔁 **Live Bitcoin price tracking** updated every 60 seconds
- 📊 Matplotlib chart with:
  - 7-day real-time price line
  - 3-day simple moving average (SMA)
- 🖥️ Terminal-based tracker with formatted output
- 📁 CSV logging for tracking price history

---

## 🚀 Technologies Used

- Python 3.13+
- `requests` for API calls
- `matplotlib` for visual plotting
- `pandas` for data manipulation
- `time`, `datetime`, `os` for live updates and formatting

---

## 📁 Project Structure

```bash
bitcoin-price-visualizer/
├── bitcoin_terminal.py        # Real-time terminal-based tracker
├── bitcoin_trend.py           # Real-time matplotlib visualizer
├── bitcoin_real_time_log.csv  # Optional log of fetched data
└── README.md                  # Project documentation
