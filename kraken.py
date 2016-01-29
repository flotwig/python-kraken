import json, urllib2

class Kraken:
	#I need three functions, one for each to retrieve Ticker, OrderBook, and Trades, and each of these functions must return an array or dict with infomration for all assets. 
	#From the page: https://www.kraken.com/help/api, please check the parts: Get ticker information,Get order book, Get recent trades. There you will find some more information on what kind of data you will return. 
	#Tip: In order to get all assets you will need to write a function that gets all assets pairs, so for that you will need as well to look at Get tradable asset pair from the api page above.
	API_BASE = 'https://api.kraken.com/0/public/'
	def getAssetPairs(self):
		return self.query('AssetPairs')
	def getAssetPairsNameString(self):
		return ','.join(self.getAssetPairs().keys())
	def getTicker(self):
		return self.query('Ticker',{'pair':self.getAssetPairsNameString()})
	def query(self,endpoint, arguments=[]):
		result = json.load(urllib2.urlopen(self.API_BASE + endpoint))
		if 'result' not in result.keys():
			raise Exception, result['error']
		else:
			return result['result']