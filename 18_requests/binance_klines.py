import requests
import pandas as pd
from datetime import date
from pathlib import Path

def get_klines(symbol, interval='1d', limit=30):
    url = "https://data-api.binance.vision/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    data = r.json()

    # Kline fields (Binance docs):
    # 0  - open time (ms since 1970-01-01 UTC)
    # 1  - open: price at the start of the day
    # 2  - high: highest price of the day
    # 3  - low: lowest price of the day
    # 4  - close: price at the end of the day
    # 5  - volume: traded amount in base asset
    # 6  - close time (ms)
    # 7  - quote asset volume: traded amount in USDT
    # 8  - number of trades
    # 9  - taker buy base asset volume (base asset)
    # 10 - taker buy quote asset volume (USDT)
    # 11 - unused, always "0"

    df = pd.DataFrame(data)

    columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']
    df = df.iloc[:, :6]
    df.columns = columns
    df['symbol'] = symbol
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df[columns[1:]] = df[columns[1:]].astype(float)

    return df

def save_raw(df, symbol):
    base_dir = Path(__file__).parent
    raw_dir = base_dir / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    file_path = raw_dir / f"{symbol}_{date.today()}.csv".replace('-', '_')
    df.to_csv(file_path, index=False)

    return file_path

def main():
    symbols = ['AAVEUSDT', 'ENAUSDT', 'RENDERUSDT', 'SOLUSDT', 'TAOUSDT']

    for symbol in symbols:
        try:
            df = get_klines(symbol)
            path = save_raw(df, symbol)
            print(f"{symbol}: {len(df)} rows -> {path.name}")
        except requests.exceptions.RequestException as err:
            print(f"{symbol}: failed - {err}")


if __name__ == "__main__":
    main()
