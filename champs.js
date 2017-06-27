
CHAMPS = function ()
{
	var champData
	var champLookup = [];
	var champDataByID = [];
	var champDetails = {};
	var key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	var baseurl = "https://na.api.pvp.net/"
	function updateData(){
		$.get("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion.json", function(data)
		{
			champData = data;
			makeChampLookup(champData.data)
		});
	}

	function makeChampLookup(champs)
	{
		for(champ in champs)
		{
			champLookup[champs[champ].key] = champs[champ];
		}
	}

	function getChampFromId(id)
	{
		return champLookup[id];
	}

	function showCamps(){
		for(var champ in champData.data)
		{
			var image = "http://ddragon.leagueoflegends.com/cdn/5.19.1/img/champion/"+champData.data[champ].image.full
			var champDiv = $('<div class="champicon" champName="'+champ+'"><span>'+champ+":<br/> "+champData.data[champ].blurb+'</span></div>');
			champDiv.css("background-image", "url(\"http://ddragon.leagueoflegends.com/cdn/5.19.1/img/champion/"+champData.data[champ].image.full+"\")");
			$.get("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/champion/"+champ+".json", function(data)
			{
				t = this.url;
				postchampname = t.split("/")[t.split("/").length-1].replace(/\.json$/g,"")
				champDetails[postchampname] = data;
			});
			$("#itemsDiv").append(champDiv);
		}

		$(".champicon").unbind().click(function(e){
			var id = this.getAttribute("champName");
			$(".champicon").css("opacity","")
			$(this).css("opacity",0.5);
			currentChamp = champData.data[id];
		});
	}
	return {updateData:updateData,showCamps:showCamps,getChampFromId:getChampFromId};
}();