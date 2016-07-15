def bfsDistancesUnweightedGraph(matrix, startVertex):
	res = []
	# _indexes = [x  for x in range(0, len(matrix))]
	# a = _indexes.pop(startVertex)
	# _indexes.insert(len(_indexes) ,a)
	_startVertex = matrix[startVertex]
	for x in range(0, len(_startVertex)):
		if not _startVertex[x]:
			res.append(0)
		else:
			res.append(1)

	# print res
	if res.count(0) > 1: # Checks if the 0 in the values is more than one
		for _id, val in enumerate(matrix[res[x]]):
			_value = 0
			if _id != startVertex and not val:
				_1d = startVertex
				# print matrix[_1d]
				while(not matrix[_1d][_id]):
					for x in matrix[_1d]:
						if x:
							_1d = matrix[_1d].index(x)
							# break
					_value += 1
				_value += 1


			if _value:
				res[_id] = _value
	print res
	return res


# bfsDistancesUnweightedGraph([[False,False,True], [False,False,True], [True,True,False]], 0) # Expected Output [0, 2, 1]
bfsDistancesUnweightedGraph([[False,True,False,False], [True,False,True,True], [False,True,False,True], [False,True,True,False]], 3) # Expected Output [2, 1, 1, 0]
# bfsDistancesUnweightedGraph([[False,True,True], [True,False,False], [True,False,False]], 0) # Expected Output [0, 1, 1]
# bfsDistancesUnweightedGraph([[0,0,1,0], [0,0,0,1], [1,0,0,1], [0,1,1,0]], 0) # Expected Output [0, 3, 1, 2]