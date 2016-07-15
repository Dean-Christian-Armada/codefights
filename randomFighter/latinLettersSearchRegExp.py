def latinLettersSearchRegExp(input):
	import re
	if len(input) < 2 or len(input) > 10:
		print 0
		return 0
	x = r'[A-Za-z]'
	obj = re.match(x, input)
	if(obj):
		print 1
		return 1
	else:
		print 0
		return 0


latinLettersSearchRegExp("a") # output = 1
latinLettersSearchRegExp("W2") # output = 1
latinLettersSearchRegExp("_1111 ") # output = 0

# Determine if the given string contains at least one letter.

# Example

# For input = "a_ _2", the output should be
# latinLettersSearchRegExp(input) = true;
# For input = "W2", the output should be
# latinLettersSearchRegExp(input) = true;
# For input = "_1111 ", the output should be
# latinLettersSearchRegExp(input) = false.
# Input/Output

# [time limit] 4000ms (py)
# [input] string input

# Constraints:
# 2 <= input.length <= 10.

# [output] boolean

# true if input contain at least one Latin letter, false otherwise.