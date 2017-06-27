
var GAMES = function ()
{
	var gamesDataList = [];
	var key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	var baseurl = "https://na.api.pvp.net/"
	function getGamesData(playerData)
	{
		var trys = 0
		UTIL.timedForeach(playerData, 1000, function(player)
		{
			if(trys>5)
			{
				return;
			}
			trys+=1
			$.get(baseurl+"/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}".replace("{region}","na").replace("{summonerId}",playerData[player].id)+key,
				function(data){
					match = data.matches[0];
					$.get(baseurl+"/api/lol/{region}/v2.2/match/{matchId}".replace("{region}","na").replace("{matchId}",match.matchId)+key+"&includeTimeline=true",
						function(data){
							gamesDataList.push(data);
						}
					);
					// data.matches.forEach(
					// 	function(match){
					// 		$.get(baseurl+"/api/lol/{region}/v2.2/match/{matchId}".replace("{region}","na").replace("{matchId}",match.matchId)+key,
					// 			function(data){
					// 					gamesDataList.push(data);
					// 			}
					// 		);
					// 	}
					// )
				}
			);
		});
	}

	function parseGame(game)
	{
		$.get("php/gamerecorded.php?gameid="+game.matchId+"&get=true",
			function(data){
				if(data == "true")
				{
					return;
				}
				$.get("php/gamerecorded.php?gameid="+game.matchId+"&get=false",
					function(data)
					{
						console.log(data);
					});
				var frames = game.timeline.frames;
				for(frame in frames)
				{
					if(frames[frame].events)
					{
						frames[frame].events.forEach(function(event)
						{
							if(event.eventType == "ITEM_PURCHASED")
							{
								$.get("php/updateChamp.php?minute="+frame+"&champID="+champ+"&itemID="+event.itemId);
							}
						});
					}
				}
			}
		)
	}
	return {getGamesData:getGamesData,parseGame:parseGame}
}();