import urllib.request
import json
import util
class CHAMPS:
	"""
	Tool for managing champs and their info
	"""
	key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	baseurl = "https://na.api.pvp.net/"
	def __init__(self):
		self.champData = []
		self.champLookup = {}
		self.champDataByID = []
		self.champDetails = {}

	def updateData(self):
		r = urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion.json")
		# with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion.json") as request:
		self.champData = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

		# stringChamps = str(request.read())
		# print(champData,"\n")
		self.makeChampLookup(self.champData["data"])

	def makeChampLookup(self, champs):
		for champ in champs:
			# print(champ,champs[champ]["key"],"\n")
			self.champLookup[int(champs[champ]["key"])] = champs[champ]

C = CHAMPS()
C.updateData()