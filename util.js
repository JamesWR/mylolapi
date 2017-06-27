UTIL = function()
{
	function timedForeach (object, timer, func) {
		var looplist = [];
		for (thing in object) {
			looplist.push(thing);
		};
		var i = 0;
		var interval = setInterval(function()
		{
			if(i>=looplist.length)
			{
				clearInterval(interval);
				return;
			}
			func(looplist[i]);
			i+=1;
		}, timer);
	}
	return {timedForeach:timedForeach};
}();