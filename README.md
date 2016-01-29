# python-kraken

python-kraken connects to the Kraken public API to pull a few data sets.

Usage:
```python
from kraken import Kraken
k = Kraken()
pairs = k.getAssetPairs()
ticker = k.getTicker()
orderbook = k.getOrderBook()
trades = k.getRecentTrades()
```

All methods are documented in [kraken.py](kraken.py) and have example output in JSON format in [examples](examples/).