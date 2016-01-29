from kraken import Kraken
import json
def writeExample(name,result):
	fp = open('examples/'+name+'.json','w+')
	json.dump(result,fp,indent=5)
	fp.close()
k = Kraken()
writeExample('getAssetPairs',k.getAssetPairs())
writeExample('getAssetPair',k.getAssetPair(k.pairs.keys()[0]))
writeExample('getTicker',k.getTicker())
writeExample('getOrderBook',k.getOrderBook())
writeExample('getRecentTrades',k.getRecentTrades())