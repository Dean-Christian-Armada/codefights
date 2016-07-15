def perfectCity(departure, destination):

	def reverseCount(count):
		if count:
			_res = abs(y[0] - x[0])
		else:
			_res = abs(y[1] - x[1])
		return _res

	x = departure
	y = destination
	if departure == destination:
		return 0
	if 0 in x:
		res = sum(x) + y[0] + y[1]
	else:
		for count in range(0, len(x)):
			if x[count] == y[count]:
				res = abs(round(x[count]) - x[count]) * 2
				res += reverseCount(count)
			else:
				if(type(x[count]) == float):
					if type(y[count]) == int:
						res = abs(y[0] - x[0]) + abs(y[1] - x[1])
					else:
						if(round(x[count]) == round(y[count])):
							res = y[count] - x[count]
						else:
							res = (y[count] - x[count]) + ((round(y[count]) - y[count]) * 2)
						res += reverseCount(count)

			# if(type(y[count]) == float):
			# 	if(round(x[count]) == round(y[count])):
			# 		res = y[count] - x[count]
			# 	else:
			# 		res = (y[count] - x[count]) + ((round(y[count]) - y[count]) * 2)
			# 	res += reverseCount(count)


	print res
	return res


perfectCity([0.2, 0], [0.5, 7]) # output 7.7
perfectCity([1, 0.4], [3, 0.9]) # output 2.7
perfectCity([0.4, 3], [0.4, 4]) # output 1.8
perfectCity([0.4, 1], [0.9, 3])  # output 2.7
perfectCity([2.4, 1], [5, 7.3]) # output 8.9
perfectCity([0, 0.2], [7, 0.5]) # output 7.7
perfectCity([0.9, 6], [1.1, 5]) # output 1.2
perfectCity([0, 0.4], [1, 0.6]) # output 2
perfectCity([1, 2.4], [7.3, 5]) # output 8.9



# (3.0 - 2.4 == .6) + 6.3 + 2 = 8.9