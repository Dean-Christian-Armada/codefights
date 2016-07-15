def isLucky(n):
	_n = str(n)
	_ln = len(_n)
	_1half = _ln / 2
	_2half = _1half
	_1half_val = _n[:_1half]
	_2half_val = _n[_2half:]

	_2half_res = [int(y) for y in _2half_val]
	_1half_res = [int(x) for x in _1half_val]

	if(sum(_2half_res) == sum(_1half_res)):
		print True
		return True
	else:
		print False
		return False


isLucky(1230) # Output = True