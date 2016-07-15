def howManySundays(n, startDay):

    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    startIndex = -1
    sunday = week.index('Sunday')
    freq = 0

    for i in range(len(week)):
        if week[i] == startDay:
            startIndex = i

    for x in range(0, n):
    	print startIndex
    	if startIndex == sunday:
    		freq += 1
    	
    	if startIndex == len(week)-1:
    		startIndex = 0
    	else:
    		startIndex += 1

    print freq
    return freq




howManySundays(9, "Saturday") # output 2
# howManySundays(7, "Sunday") # output 1
# howManySundays(6, "Monday") # output 0
# howManySundays(4, "Wednesday") # output 0