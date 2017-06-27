
SUMMONERS = function()
{
	var key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	var baseurl = "https://na.api.pvp.net/"
	var summonerDetails = {};
	function updateData(){

		$.get(baseurl+"observer-mode/rest/featured"+key, function(data)
		{
			var gamesList = data.gameList;
			gamesList.forEach(function(game)
			{
				updateSummonerData(game.participants[0].summonerName);
			});
		});
	}

	function getSummonerData(name)
	{
		if(typeof name == typeof undefined)
		{
			return summonerDetails;
		}
		else
		{
			return summonerDetails[name];
		}
	}

	function getSummonerList()
	{
		var summonerlist = [];
		for(summoner in summonerDetails)
		{
			summonerlist.push(summoner);
		}
		return summonerlist;
	}

	function updateSummonerData(name)
	{
		var toreturn;
		$.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+name+key, function(data)
		{
			for(player in data)
			{
				summonerDetails[name]=data[player];
			}
		});
	}
	return {updateData:updateData,getSummonerData:getSummonerData,getSummonerList:getSummonerList};
}();