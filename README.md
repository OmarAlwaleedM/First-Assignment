# Finance Data Fetcher (Python)

This project was created for a Python coding class and demonstrates how to fetch up-to-date financial data from the internet using Python. The user can choose which stock to analyze at runtime.

## Features

* Fetches daily stock OHLCV data from the public Stooq data source (no API key required)
* Allows the user to input a desired stock symbol (e.g. AAPL, TSLA, MSFT.US)
* Displays the latest closing price and trading volume
* Computes a simple 30-day annualized volatility estimate
* Compares the latest trading volume to the 30-day average

## Example Usage

```bash
python main.py
```

When prompted, enter a stock symbol:

```text
Enter a stock symbol (e.g., AAPL or AAPL.US): AAPL
```

## Example Output

```text
Symbol: AAPL.US
Latest trading day: 2026-01-16
Close: 255.53
Volume: 72,142,773
30-day annualized volatility (rough): 10.38%
Volume is above the 30-day average (higher-than-usual trading activity).
```

## How It Works

* The program downloads daily price data as a CSV file from Stooq.
* Daily returns are computed from closing prices.
* Volatility is calculated using the standard deviation of the last 30 daily returns and annualized assuming 252 trading days per year.

## Requirements

* Python 3.9+
* pandas

Install dependencies with:

```bash
pip install pandas
```

## Data Source

Daily stock data is provided by Stooq ([https://stooq.com](https://stooq.com)) via a public CSV endpoint.

## Author

Omar Ibrahim
