

var champDetails = {};
var currentChamp;
ITEMS = function()
{

	var key = "?api_key=39b6900e-5eea-4b0f-b3e2-afc5db2a7c55"
	var baseurl = "https://na.api.pvp.net/"
	var itemData;
	var currentItem
	function updateData(){
		$.get("http://ddragon.leagueoflegends.com/cdn/5.19.1/data/en_US/item.json", function(data)
		{
			itemData = data;
		});
	}

	function showItems(){
		for(var item in itemData.data)
		{
			var image = "http://ddragon.leagueoflegends.com/cdn/5.19.1/img/item/"+itemData.data[item].image.full
			var itemDiv = $('<div class="itemicon" itemID='+item+' itemName="'+itemData.data[item].name+'"><span>'+itemData.data[item].name+":<br/> "+itemData.data[item].description+'</span></div>');
			itemDiv.css("background-image", "url(\"http://ddragon.leagueoflegends.com/cdn/5.19.1/img/item/"+itemData.data[item].image.full+"\")");
			$("#itemsDiv").append(itemDiv);
		}
		$("#itemsDiv").append("<br>");
		$(".itemSearch").keyup(function(e)
		{
			itemSearchApply($(this).val());
		});
		$(".itemicon").unbind().click(function(e){
			var id = this.getAttribute("itemID");
			$(".itemicon").css("opacity","")
			$(this).css("opacity",0.5);
			currentItem = itemData.data[id];
		});
	}

	function itemSearchApply(searchChars)
	{
		items = $(".itemicon");
	    for(i =0; i < items.length; i++)
	    {
	        //alert(items[i]);

	        if(items[i].getAttribute("itemName").toLowerCase().indexOf(searchChars.toLowerCase()) == -1)
	        {
	            $(items[i]).hide();
	            // alert("hide div");
	        }
	        else
	        {
	            $(items[i]).show();
	        }
	    }
	}
	return {updateData:updateData,showItems:showItems};
}();