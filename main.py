import pandas as pd


def fetch_stooq_daily(symbol: str) -> pd.DataFrame:
    """
    Fetches daily OHLCV data from Stooq as a pandas DataFrame.
    Example symbol formats: 'aapl.us', 'msft.us', 'tsla.us'
    """
    url = f"https://stooq.com/q/d/l/?s={symbol.lower()}&i=d"
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def normalize_symbol(user_input: str) -> str:
    """
    Normalize user input to a Stooq symbol format.
    If the user types 'AAPL' we assume US stocks and convert to 'aapl.us'.
    If they already typed 'aapl.us' we keep it.
    """
    s = user_input.strip().lower()
    if not s:
        raise ValueError("Empty symbol.")

    # If user didn't include a market suffix, default to US
    if "." not in s:
        s = f"{s}.us"

    return s


def main():
    raw = input("Enter a stock symbol (e.g., AAPL or AAPL.US, TSLA, MSLE): ").strip()
    symbol = normalize_symbol(raw)

    try:
        df = fetch_stooq_daily(symbol)
    except Exception as e:
        print(f"Error fetching data for '{symbol.upper()}': {e}")
        return

    if df.empty:
        print(f"No data returned for '{symbol.upper()}'. Try a different symbol.")
        return

    latest = df.iloc[-1]

    print(f"\nSymbol: {symbol.upper()}")
    print(f"Latest trading day: {latest['Date'].date()}")
    print(f"Close: {latest['Close']}")
    print(f"Volume: {int(latest['Volume']):,}")

    # mini analysis
    df["DailyReturn"] = df["Close"].pct_change()
    last_30 = df.tail(30).copy()

    vol_30 = last_30["DailyReturn"].std() * (252 ** 0.5)  # annualized volatility
    print(f"30-day annualized volatility (rough): {vol_30:.2%}")

    # compare latest volume to 30-day average volume
    avg_volume_30 = last_30["Volume"].mean()
    if latest["Volume"] > avg_volume_30:
        print("Volume is above the 30-day average (higher-than-usual trading activity).")
    else:
        print("Volume is below the 30-day average.")


if __name__ == "__main__":
    main()
