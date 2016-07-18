def parkingSpot(carDimensions, parkingLot, luckySpot):
	cD = carDimensions
	l = cD[0] # length
	w = cD[1] # width 
	lS = luckySpot
	# This method is used to make sure if the luckySpot is compatible with carDimensions
	def isParkable(lS, cD):
		if(lS[2] - lS[0] + 1 == cD[0] and lS[3] - lS[1] + 1 == cD[1]):
			cond = 1
			return (True, cond)
		elif(lS[2] - lS[0] + 1 == cD[1] and lS[3] - lS[1] + 1 == cD[0]):
			cond = 2
			return (True, cond)
		else:
			return (False, False)

	iP = isParkable(lS, carDimensions)

	if iP[0]: # If luckySpot is compatible with carDimensions
		spots = [] # This is where all the parking coordinates will be stored

		# Determines the parking coordinates for the carDimension
		# Please be informed that luckySpot plays a great role on determining the parking coordinates
		# The trick is the first two indexes is actually the [x, y] of the starting coordinate of the parking
		# And the last two indexes is actullay the [x, y] of the last coordinate of the parking
		for x in range(lS[0], lS[2]+1):
			for y in range(lS[1], lS[3]+1):
				spots.append([ x, y ]) # Creates the matrix of the parking coordinates

		print spots

		# These two is where the coordinates before the parking spot is stored
		# Basically, these edges will be used to determine if the parking Spot has no obstacles for the car to enter
		# If there is an obstacle then it cannot be parked
		_edgeX = []
		_edgeY = []

		for edges in spots:
			if edges[0] not in _edgeX:
				_edgeX.append(edges[0]) # Gets all the points that are used as a coordinate in the x-axis
			if edges[1] not in _edgeY:
				_edgeY.append(edges[1]) # Gets all the points that are used as a coordinate in the y-axis


		# START, determines if there is an obstacle for the parking
		# PLEASE take note that the parking spot can be entered after and before the coordinates ===== (4,5)[after] and (4, 0)[before]

		# If the condition is 1, then most likely it is parked vertically, making the y-axis points a very important factor for the spot
		if iP[1] == 1: # If the luckySpot condition is 1 ======  lS[2] - lS[0] + 1 == cD[0] and lS[3] - lS[1] + 1 == cD[1]
			for y in _edgeY:
				_list = []
				for x in range(min(_edgeX), 0, -1): # What this does is, it checks every point on the y-axis before the parking spot if there is an obstacle
					if parkingLot[x-1][y]:
						_list.append([x-1, y])

				for x in range(max(_edgeX)+1, len(parkingLot)): # What this does is, it checks every point on the y-axis after the parking spot if there is an obstacle
					if parkingLot[x][y]:
						_list.append([x, y])

				if len(_list) > 1: # If there is an obstacle both before and after then the parking spot is not parkable
					print 0
					return 0
		# If the condition is 0, then most likely it is parked horizontally, making the x-axis points a very important factor for the spot
		else:  # If the luckySpot condition is 1 ======  lS[2] - lS[0] + 1 == cD[1] and lS[3] - lS[1] + 1 == cD[0]
			for x in _edgeX:
				_list = []
				for y in range(min(_edgeY), 0, -1):  # What this does is, it checks every point on the x-axis before the parking spot if there is an obstacle
					if parkingLot[x][y-1]:
						_list.append([x, y-1])

				for y in range(max(_edgeY)+1, len(parkingLot[x])):  # What this does is, it checks every point on the x-axis after the parking spot if there is an obstacle
					if parkingLot[x][y]:
						_list.append([x, y])

				if len(_list) > 1: # If there is an obstacle both before and after then the parking spot is not parkable
					print 0
					return 0
		# END, determines if there is an obstacle for the parking

		# Checks if every coordinate of the parking spot available
		# If there is even a single obstacle then it is not parkable
		for x in spots:
			if parkingLot[x[0]][x[1]]:
				print 0
				return 0

		# If every condition that makes the parking spot unparkable fails then it is safe to say that it can be parked
		print 1
		return 1

	else: # if luckySpot is not compatible with the carDimensions
		return 0

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

# # # # Output false
parkingSpot(
	[4, 1], 
	[	
		[1,1,1,1,1,1], 
		[1,0,1,0,1,0], 
		[1,0,0,0,1,0], 
		[0,0,0,0,0,1], 
		[1,0,0,0,1,1],
		[1,1,1,0,1,1],
	],
	[1, 3, 4, 3]
)

# # # # Output true
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
# # (3-0) + 1 = 4
# # (3-3) + 1 = 1
# # (0, 3)
# # (3, 3)

# # [0, 3], [1, 3], [2, 3], [3, 3]

# # [0, 3], [3, 3]

# # # Output true
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
# # (7-1) + 1 = 7
# # (1-0) + 1 = 2
# # (7, 1)
# # (0, 1)
# # [1, 0], [7, 1]
# # [1, 0], [7, 0], [1, 1], [7, 1]

# # # Output true
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
# # (2-1) + 1 = 2
# # (3-1) + 1 = 3

# # [1, 1], [1, 2], [1, 3]
# # [2, 1], [2, 2], [2, 3]

# # [1, 1], [2, 3]

# # # # Output true
# parkingSpot(
# 	[2, 1], 
# 	[	
# 		[1,0,1], 
# 		 [1,0,1], 
# 		 [1,1,1]
# 	],
# 	[0, 1, 1, 1]
# )
# # (1-0) + 1 = 2
# # (1-1) + 1 = 1
# # (0, 2)
# # (0, 1)
# # [0, 1], [1, 1]

# # # Output true
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1,1], 
# 		[1,0,0,0], 
# 		[1,0,1,0]
# 	],
# 	[1, 2, 1, 3]
# )
# # [1-1] + 1 = 1
# # [3-2] + 1 = 2
# # (1, 1)
# # (2, 3)
# # [1, 2], [1, 3]

# # # Output true
# parkingSpot(
# 	[7, 2],
# 	[	
# 		[0,0,0,0,0,0,0,0], 
# 		[1,0,0,0,0,0,0,0], 
# 		[0,0,0,0,0,0,0,0]
# 	],
# 	[1, 1, 2, 7]
# )
# # (2-1) + 1 = 2
# # (7-1) + 1 = 7
# # (0, 3)
# # (3, 3)
# # [1, 1], [1, 7], [2, 1], [2, 7]

# # # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,0,1], 
# 		[1,0,1], 
# 		[1,1,1]
# 	],
# 	[1, 1, 2, 1]
# )
# # (2-1) + 1 = 2
# # (1-1) + 1 = 1
# # (1, 2)
# # (1, 1)

# # # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1], 
# 		[1,0,1], 
# 		[1,1,1]
# 	],
# 	[0, 1, 1, 1]
# )
# # (1-0) + 1 = 2
# # (1-1) + 1 = 1
# # (0, 1)
# # (1, 1)

# # # Output false
# parkingSpot(
# 	[2, 1],
# 	[	
# 		[1,1,1,1], 
# 		[1,0,0,0], 
# 		[1,0,1,0]
# 	],
# 	[2, 1, 2, 2]
# )
# # (2-1) + 1 = 1
# # (2-1) + 1 = 2
# # (2, 2)
# # (1, 2)

# # # # Output false
# parkingSpot(
# 	[4, 2], 
# 	[	
# 		[0,0,0,1], 
# 		[0,0,0,0], 
# 		[0,0,1,1]
# 	],
# 	[0, 0, 1, 3]
# )

# # # Output false
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

# # # Output false
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