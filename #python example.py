#python example

class ExampleClass(object):
	def __init__(self, exampleInitInput):
		self.exampleInitVal = exampleInitInput

	def exampleMemberFunction(self, exampleVar):
		l=[1,2,5,-1]
		nl = sorted(t)
		l.sort() # s and t are now sorted t
		ifval = "a" if True else "b"

		minInt = -sys.maxint - 1

		l= [1,2,4,5]
		bisect.insort_left(l,3) # l has 3 in correct place
		heapq.heapify(l)#make heap of l
		heapq.heappush(6)#efficient heap push
		heapq.heappop()#efficient get min from l


for i in range(1,1):
	print(i)