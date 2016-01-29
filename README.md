# python-kraken

python-kraken connects to the Kraken public API to pull a few data sets.

Usage:
```python
from kraken import Kraken
k = Kraken()
trades = k.getRecentTrades()
```

All methods are documented in kraken.py and have example output in JSON format in [examples](examples/).