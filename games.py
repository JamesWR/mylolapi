import urllib.request
import json
import time
from util import UTIL as util
from summoners import SUMMONERS as summoners
class GAMES:
	"""
	Tool getting game data and push data to data base
	"""
	key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	baseurl = "https://na.api.pvp.net/"
	summonerurl = "/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}"
	matchurl = "/api/lol/{region}/v2.2/match/{matchId}"

	def __init__(self, maxTrys):
		self.gamesDataList = []
		self.maxTrys = maxTrys

	def getGamesData(self, playerData):
		trys = 0 # opional limit on posts
		while trys<=self.maxTrys:
			trys+=1
			url = GAMES.baseurl+(GAMES.summonerurl).replace("{region}","na").replace("{summonerId}",str(playerData["id"]))+GAMES.key
			print(url)
			r = urllib.request.urlopen(url)
			match = util.jsonParse(r)["matches"][0]
			print(match)
			r = urllib.request.urlopen(GAMES.baseurl+GAMES.matchurl.replace("{region}","na").replace("{matchId}",str(match["matchId"]))+self.key+"&includeTimeline=true")
			self.gamesDataList.append(util.jsonParse(r))
			# time.sleep(1)



	def updateData(self):
		r = urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion.json")
		# with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion.json") as request:
		champData = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

		# stringChamps = str(request.read())
		# print(champData,"\n")
		self.makeChampLookup(champData["data"])

	def makeChampLookup(self, champs):
		for champ in champs:
			# print(champ,champs[champ]["key"],"\n")
			self.champLookup[int(champs[champ]["key"])] = champs[champ]

	def parseGames(self, games):
		r = urllib.request.urlopen("php/gamerecorded.php?gameid="+str(game["matchId"])+"$get=true");
		indatabase = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
		if(data = "true"):
			return
		else:
			r =

s = summoners(3,3)
s.updateData()
g = GAMES(1)
summonersUsed = 0
for summoner in s.summonerDetails:
	summonersUsed += 1
	if summonersUsed > 2:
		print("!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!")
		break
	print(s.summonerDetails[summoner])
	g.getGamesData(s.summonerDetails[summoner])

# summonerurl = "/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}"
# print(summonerurl.replace("{region}","na").replace("{summonerId}","thing")+"key")
# print(summonerurl)