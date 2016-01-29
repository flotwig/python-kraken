import json, urllib2
from urllib import urlencode

class Kraken:
	"""Short class to interact with Kraken public API.
	
	Public methods:
	getAssetPair
	getAssetPairs
	getTicker
	getOrderBook
	getRecentTrades
	"""
	API_BASE = 'https://api.kraken.com/0/public/'
	def __init__(self):
		self.pairs = self.getAssetPairs()
	def getAssetPairs(self):
		"""Get all asset pairs. Will cache between requests.
		"""
		if hasattr(self,'pairs'):
			return self.pairs
		else:
			return self._query('AssetPairs')
	def getAssetPair(self,name):
		"""Return a single asset pair by name.
		
		Argument:
		name	-- The name of the asset pair.
		"""
		return self.pairs.get(name)
	def getTicker(self):
		"""Get a ticker for all asset pairs.
		"""
		return self._joinPairs(self._query('Ticker',{'pair':self._getAssetPairsNameString()}))
	def getOrderBook(self):
		"""Get an order book for all asset pairs. Requires one query per asset pair.
		"""
		book = {}
		for pair in self.pairs:
			if(pair[-2] != '.'):
				book[pair] = self._query('Depth',{'pair':pair})
		return self._joinPairs(book)
	def getRecentTrades(self):
		"""Gets recent trades for all asset pairs. Requires one query per asset pair.
		"""
		trades = {}
		for pair in self.pairs:
			if(pair[-2] != '.'):
				trades[pair] = self._query('Trades',{'pair':pair})
		return self._joinPairs(trades)
	def _getAssetPairsNameString(self):
		"""Helper method which returns all valid asset pair names concatenated with a comma.
		"""
		return ','.join(self.pairs.keys())
	def _joinPairs(self,result):
		"""Helper method which joins a result set with the asset pair information.
		
		Argument:
		result	-- The Object result of a _query call.
		"""
		for rkey in result.keys():
			result[rkey]['asset'] = self.pairs[rkey]
		return result
	def _query(self,endpoint, arguments={}):
		"""Connects to the Kraken API, executes a query, and returns the result as a Python object.
		
		Arguments:
		endpoint	-- The string name of the endpoint to call.
		arguments	-- A dict of arguments to add on.
		"""
		url = self.API_BASE + endpoint
		result = json.load(urllib2.urlopen(url,urlencode(arguments)))
		if 'result' not in result.keys():
			raise Exception(result['error'])
		else:
			return result['result']