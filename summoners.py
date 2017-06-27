import urllib
import json
import time
from util import UTIL as util
class SUMMONERS:
	key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	baseurl = "https://na.api.pvp.net/"
	summonerurl = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"
	def __init__(self, delay, count):
		self.summonerDetails = {};
		self.delay = delay
		self.count = count
	def updateData(self):
		r = urllib.request.urlopen(SUMMONERS.baseurl+"observer-mode/rest/featured"+SUMMONERS.key)
		gamesList = util.jsonParse(r)["gameList"]
		i = 0
		for game in gamesList:
			if i > self.count:
				return
			i+=1
			self.updateSummonerData((game["participants"][0])["summonerName"]);
			time.sleep(self.delay)



	# function getSummonerData(name):
	# 	if(typeof name == typeof undefined):
	# 		return summonerDetails
	# 	else:
	# 		return summonerDetails[name]


	# function getSummonerList()
	# {
	# 	var summonerlist = [];
	# 	for(summoner in summonerDetails)
	# 	{
	# 		summonerlist.push(summoner);
	# 	}
	# 	return summonerlist;
	# }

	def updateSummonerData(self, name):
		url = SUMMONERS.summonerurl+urllib.parse.quote(name, '')+SUMMONERS.key;
		# print(url)
		r = urllib.request.urlopen(url)
		players = util.jsonParse(r)
		# print(name)
		for player in players:
			# print(players[player])
			self.summonerDetails[name]=players[player];

# S = SUMMONERS()
# S.updateData()
# t= [1,2,3]
# print(t[0:2])