import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
except HTTPError as e:
    print("HTTP error:", e.code)
except URLError as e:
    print("Connection error:", e.reason)
else:
    print("Number of currencies:", len(data))

    items = []
    for item in data:
        if item.get("Ccy") in ("USD", "EUR", "RUB"):
            items.append(item)
            print(item["Ccy"], item["Rate"], item["Date"])
            if item["Ccy"] == "USD":
                print(f"$100 = {100 * float(item['Rate']):,.2f} SUM")

    with open("rates.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    max_diff = 0.0
    most_changed = None
    for item in data:
        diff = abs(float(item["Diff"]))
        if diff > max_diff:
            max_diff = diff
            most_changed = item

    if most_changed:
        print("Most changed:", most_changed["Ccy"], most_changed["Diff"])
