import json, urllib2
from urllib import urlencode

class Kraken:
	API_BASE = 'https://api.kraken.com/0/public/'
	def __init__(self):
		self.pairs = self.getAssetPairs()
	def getAssetPairs(self):
		if hasattr(self,'pairs'):
			return self.pairs
		else:
			return self.query('AssetPairs')
	def getAssetPair(self,name):
		return self.pairs.get(name)
	def getAssetPairsNameString(self):
		return ','.join(filter(lambda pair: pair[-2]!='.',self.pairs.keys()))
	def getTicker(self):
		return self.joinPairs(self.query('Ticker',{'pair':self.getAssetPairsNameString()}))
	def getOrderBook(self):
		book = {}
		for pair in self.pairs:
			if(pair[-2] != '.'):
				book[pair] = self.query('Depth',{'pair':pair})
		return self.joinPairs(book)
	def getRecentTrades(self):
		trades = {}
		for pair in self.pairs:
			if(pair[-2] != '.'):
				trades[pair] = self.query('Trades',{'pair':pair})
		return self.joinPairs(trades)
	def joinPairs(self,result):
		for rkey in result.keys():
			result[rkey]['asset'] = self.pairs[rkey]
		return result
	def query(self,endpoint, arguments={}):
		url = self.API_BASE + endpoint
		result = json.load(urllib2.urlopen(url,urlencode(arguments)))
		if 'result' not in result.keys():
			raise Exception(result['error'])
		else:
			return result['result']