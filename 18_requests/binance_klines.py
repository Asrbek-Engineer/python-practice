import requests
import pandas as pd
from datetime import date
from pathlib import Path

url = "https://data-api.binance.vision/api/v3/klines"
params = {"symbol": "SOLUSDT", "interval": "1d", "limit": 30}

r = requests.get(url, params=params, timeout=10)
print(r.status_code)
r.raise_for_status()

data = r.json()
print(type(data))
print(len(data))
print(data[0])

for i, v in enumerate(data[0]):
    print(i, v)

# Kline fields (Binance docs):
# 0  - open time (ms since 1970-01-01 UTC)
# 1  - open: price at the start of the day
# 2  - high: highest price of the day
# 3  - low: lowest price of the day
# 4  - close: price at the end of the day
# 5  - volume: traded amount in SOL
# 6  - close time (ms)
# 7  - quote asset volume: traded amount in USDT
# 8  - number of trades
# 9  - taker buy base asset volume (SOL)
# 10 - taker buy quote asset volume (USDT)
# 11 - unused, always "0"

df = pd.DataFrame(data)
print(df.shape)
print(df.head())

columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']
df = df.iloc[:, :6]
df.columns = columns
print(df.head())
print(df.dtypes)

df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
print(df.dtypes)

df[columns[1:]] = df[columns[1:]].astype(float)
print(df.dtypes)

print(len(df))
print(df.isna().sum())
print(df['open_time'].duplicated().sum())

base_dir = Path(__file__).parent
raw_dir = base_dir / "data" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

file_path = raw_dir / f"SOLUSDT_{date.today()}.csv".replace('-', '_')
df.to_csv(file_path, index=False)
