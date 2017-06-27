def minimal_sub_array(array):
	"""
	:type array: List[int]
	:rtype: List[int]
	"""
	minsum = 0
	min_i = 0
	min_j = 0
	for i in range(len(array)):
		newsum = array[i]
		for j in range(i+1,len(array)):
			newsum += array[j]
			print(i,j,newsum)
			if newsum < minsum:
				minsum = newsum
				min_i = i
				min_j = j
	return array[min_i:min_j]
print(minimal_sub_array([-1,2,-3])