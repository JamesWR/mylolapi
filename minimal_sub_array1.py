def minimal_sub_array(array):
	"""
	:type array: List[int]
	:rtype: List[int]
	"""
	minsum = 0
	min_i = 0
	min_j = 0
	for i in range(len(array)):
		newsum = 0
		for j in range(i,len(array)):
			newsum += array[j]
			if newsum < minsum:
				minsum = newsum
				min_i = i
				min_j = j+1
	return array[min_i:min_j]