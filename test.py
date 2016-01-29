import kraken

k = kraken.Kraken()
pairs = k.getAssetPairs()
ticker = k.getTicker()
orderbook = k.getOrderBook()
trades = k.getRecentTrades()