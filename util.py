import time
import urllib.request
import json
class UTIL:
	thing = "nothing"
	def timedForeach(object, timer, func):
		looplist = []
		for thing in object:
			func(thing)
			time.sleep(timer)

	def jsonParse(data):
		return json.loads(data.read().decode(data.info().get_param('charset') or 'utf-8'))

	def jsonGet(url):
		r = urllib.request.urlopen(url);
		result = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
		return result

t= [1,2,3,4,5]
t.append(6)
print(max(1,2))