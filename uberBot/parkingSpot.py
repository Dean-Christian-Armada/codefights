def parkingSpot(carDimensions, parkingLot, luckySpot):
	cD = carDimensions
	l = cD[0] # length
	w = cD[1] # width 
	lS = luckySpot
	def isParkable(lS, cD):
		if(lS[2] - lS[0] + 1 == cD[0] and lS[3] - lS[1] + 1 == cD[1]):
			return True
		elif(lS[2] - lS[0] + 1 == cD[1] and lS[3] - lS[1] + 1 == cD[0]):
			return True
		else:
			return False

	if isParkable(lS, carDimensions):
		numOfSpots = l * w
		spots = []
		spots.append([lS[0], lS[1]])
		spots.append([lS[2], lS[3]])

		_x = (lS[2]-lS[0]) + 1
		_y = (lS[3]-lS[1]) + 1

		count = 1

		if _x == l:
			spot_x = spots[0][0]
			spot_y = spots[0][1]
		else:
			spot_x = spots[1][0]
			spot_y = spots[1][1]

		# for x in range(spot_x, _x):
		# 	if [x, spot_y] not in spots:
		# 		spots.insert(count, [x, spot_y])
		# 	for y in range(spot_y, _y):
		# 		if [y, spot_y] not in spots:
		# 			spots.insert(count, [y, spot_y])
		# 	count += 1

		# for x in range(spots[0][0], cD[0]+1):
		# 	if [spots[0][0], x] not in spots:
		# 		spots.insert(count, [spots[0][0], x])
		# 	for y in range(spots[0][1], cD[1]+1):
		# 		if [y, x] not in spots:
		# 			spots.insert(count, [y, x])
		# 	count += 1

		# for y in range(spots[0][1], cD[1]):
		# 	if [y, x] not in spots:
		# 		spots.insert(count, [y, x])
		# 	for x in range(spots[0][1], cD[1]):
		# 		if [spots[0][0], x] not in spots:
		# 			spots.insert(count, [spots[0][0], x])
		# 	count += 1

		# while(len(spots) < numOfSpots):
		# 	# spots.insert(count, [])
		# 	# TODO: know the increment of the coordinates, WHICH IS WHICH?
		# 	count += 1

		# print spots

		for x in spots:
			if parkingLot[x[0]][x[1]]:
				print 0
				return 0

		print 1
		return 1

	else:
		return 0

# # Output true
# parkingSpot(
# 	[7, 2], 
# 	[	
# 		[0,1,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0]
# 	],
# 	[1, 0, 7, 1]
# )
# (7-1) + 1 = 7
# (1-0) + 1 = 2
# (7, 1)
# (0, 1)
# [1, 0], [7, 1]
# [1, 0], [7, 0], [1, 1], [7, 1]

_x = []
array = [7, 2]
array2 = [1, 0, 7, 1]
# _x = []
# array = [4, 1]
# array2 = [0, 3, 3, 3]

# [[0, 3], [1, 3], [2, 3], [3, 3]]
# [4, 1]
# [0, 3, 3, 3]
# cond 1
# for x in range(0, 4):
# 	for y in range(3, 4):
# 		_x.append([x, y])

# [7, 2]
# [1, 0, 7, 1]
# [1, 0], [7, 0], [1, 1], [7, 1]
# cond 1
# for x in range(1, 8):
# 	for y in range(0, 2):
# 		_x.append([ x, y ])

# [1, 1], [1, 2], [1, 3]
# [2, 1], [2, 2], [2, 3]
# [3, 2], 
# [1, 1, 2, 3]
# cond 2
# for x in range(1, 3):
# 	for y in range(1, 4):
# 		_x.append([ x, y ])

# [7, 2],
# [1, 1, 2, 7]
# [1, 1], [1, 7], [2, 1], [2, 7]
# cond 2
# for x in range(1, 3):
# 	for y in range(1, 8):
# 		_x.append([ x, y ])

# [2, 1], 
# [0, 1, 1, 1]
# [0, 1], [1, 1]
# cond 1
for x in range(0, 2):
	for y in range(1, 2):
		_x.append([ x, y ])

print _x

# # # Output true
# parkingSpot(
# 	[4, 1], 
# 	[	
# 		[1,0,1,0,1,0], 
# 		[1,0,0,0,1,0], 
# 		[0,0,0,0,0,1], 
# 		[1,0,0,0,1,1]
# 	],
# 	[0, 3, 3, 3]
# )
# (3-0) + 1 = 4
# (3-3) + 1 = 1
# (0, 3)
# (3, 3)

# [0, 3], [1, 3], [2, 3], [3, 3]

# [0, 3], [3, 3]

# # Output true
# parkingSpot(
# 	[7, 2], 
# 	[	
# 		[0,1,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0]
# 	],
# 	[1, 0, 7, 1]
# )
# (7-1) + 1 = 7
# (1-0) + 1 = 2
# (7, 1)
# (0, 1)
# [1, 0], [7, 1]
# [1, 0], [7, 0], [1, 1], [7, 1]

# # Output true
# parkingSpot(
# 	[3, 2], 
# 	[
# 		[1,0,1,0,1,0], 
# 		[0,0,0,0,1,0], 
# 		[0,0,0,0,0,1], 
# 		[1,0,1,1,1,1]
# 	],
# 	[1, 1, 2, 3]
# )
# (2-1) + 1 = 2
# (3-1) + 1 = 3

# [1, 1], [1, 2], [1, 3]
# [2, 1], [2, 2], [2, 3]

# [1, 1], [2, 3]

# # # Output true
# parkingSpot(
# 	[2, 1], 
# 	[	
# 		[1,0,1], 
# 		 [1,0,1], 
# 		 [1,1,1]
# 	],
# 	[0, 1, 1, 1]
# )
# (1-0) + 1 = 2
# (1-1) + 1 = 1
# (0, 2)
# (0, 1)
# [0, 1], [1, 1]

# # Output true
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1,1], 
# 		[1,0,0,0], 
# 		[1,0,1,0]
# 	],
# 	[1, 2, 1, 3]
# )
# [1-1] + 1 = 1
# [3-2] + 1 = 2
# (1, 1)
# (2, 3)
# [1, 2], [1, 3]

# # Output true
# parkingSpot(
# 	[7, 2],
# 	[	
# 		[0,0,0,0,0,0,0,0], 
# 		[1,0,0,0,0,0,0,0], 
# 		[0,0,0,0,0,0,0,0]
# 	],
# 	[1, 1, 2, 7]
# )
# (2-1) + 1 = 2
# (7-1) + 1 = 7
# (0, 3)
# (3, 3)
# [1, 1], [1, 7], [2, 1], [2, 7]

# # Output false
# parkingSpot(
# 	[3, 2], 
# 	[	
# 		[1,0,1,0,1,0], 
# 		[1,0,0,0,1,0], 
# 		[0,0,0,0,0,1], 
# 		[1,0,0,0,1,1]
# 	],
# 	[1, 1, 2, 3]
# )

# # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,0,1], 
# 		[1,0,1], 
# 		[1,1,1]
# 	],
# 	[1, 1, 2, 1]
# )
# (2-1) + 1 = 2
# (1-1) + 1 = 1
# (1, 2)
# (1, 1)

# # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1], 
# 		[1,0,1], 
# 		[1,1,1]
# 	],
# 	[0, 1, 1, 1]
# )
# (1-0) + 1 = 2
# (1-1) + 1 = 1
# (0, 1)
# (1, 1)

# # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1,1], 
# 		[1,0,0,0], 
# 		[1,0,1,0]
# 	],
# 	[2, 1, 2, 2]
# )
# (2-1) + 1 = 1
# (2-1) + 1 = 2
# (2, 2)
# (1, 2)

# # # Output false
# parkingSpot(
# 	[4, 2], 
# 	[	
# 		[0,0,0,1], 
# 		[0,0,0,0], 
# 		[0,0,1,1]
# 	],
# 	[0, 0, 1, 3]
# )

# # Output false
# parkingSpot(
# 	[7, 2], 
# 	[	
# 		[0,1,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,0,0], 
# 		[0,1,0]
# 	],
# 	[1, 0, 7, 1]
# )

# # Output false
# parkingSpot(
# 	[5, 3],
# 	[	
# 		[1,1,1,1,1,0,1,1,1,1], 
# 		[0,1,0,0,1,0,0,0,0,0], 
# 		[0,0,0,0,0,0,0,0,1,0], 
# 		[0,0,0,0,0,0,0,0,0,0], 
# 		[0,0,0,0,0,0,0,0,0,1], 
# 		[0,0,0,0,0,0,0,0,1,0], 
# 		[0,0,1,0,0,0,0,0,0,0], 
# 		[1,0,0,0,0,0,0,0,0,0]
# 	],
# 	[1, 3, 5, 5]
# )
# (5-1) + 1 = 5
# (5-3) + 1 = 3
# (2, 2)
# (1, 2)
# [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5],








# This time you are an Uber driver and you are trying your best to park your car in a parking lot.

# Your car has length carDimensions[0] and width carDimensions[1]. You have already picked your lucky spot (rectangle of the same size as the car with upper left corner at (luckySpot[0], luckySpot[1])) and bottom right corner at (luckySpot[2], luckySpot[3]) and you need to find out if it's possible to park there or not.

# It is possible to park your car at a given spot if and only if you can drive through the parking lot without any turns to your lucky spot (for safety reasons, the car can only move in two directions inside the parking lot - forwards or backwards along the long side of the car) starting from some side of the lot. Assume that the car can't drive through or park at any of the occupied spots.

# Example

# For carDimensions = [3, 2],

# parkingLot = [[1, 0, 1, 0, 1, 0],
#               [0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 1],
#               [1, 0, 1, 1, 1, 1]]
# and
# luckySpot = [1, 1, 2, 3], the output should be
# parkingSpot(carDimensions, parkingLot, luckySpot) = true.



# For carDimensions = [3, 2],

# parkingLot = [[1, 0, 1, 0, 1, 0],
#               [1, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 1],
#               [1, 0, 0, 0, 1, 1]]
# and
# luckySpot = [1, 1, 2, 3], the output should be
# parkingSpot(carDimensions, parkingLot, luckySpot) = false;

# For carDimensions = [4, 1],
# the same parkingLot as in the previous example and
# luckySpot = [0, 3, 3, 3], the output should be
# parkingSpot(carDimensions, parkingLot, luckySpot) = true.

# Input/Output

# [time limit] 4000ms (py)
# [input] array.integer carDimensions

# Array of two positive integers. It is guaranteed that carDimensions[0] > carDimensions[1].

# Constraints:
# 1 <= carDimensions[i] <= 10.

# [input] array.array.integer parkingLot

# 2-dimensional array, where parkingLot[x][y] is 1 if cell (x, y) is occupied and is 0 otherwise.

# Constraints:
# 3 <= parkingLot.length <= 10,
# 3 <= parkingLot[0].length <= 10.

# [input] array.integer luckySpot

# Array of four integers - coordinates of your lucky spot at the parking lot.
# It is guaranteed that one of the following statements is true:

# luckySpot[2] - luckySpot[0] + 1 = carDimensions[0] and
# luckySpot[3] - luckySpot[1] + 1 = carDimensions[1];
# luckySpot[2] - luckySpot[0] + 1 = carDimensions[1] and
# luckySpot[3] - luckySpot[1] + 1 = carDimensions[0].
# Constraints:
# 0 <= luckySpot[0] <= luckySpot[2] < parkingLot.length,
# 0 <= luckySpot[1] <= luckySpot[3] < parkingLot[i].length.

# [output] boolean

# true if it is possible to park your car, false otherwise.