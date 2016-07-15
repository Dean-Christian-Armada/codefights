def countSumOfTwoRepresentations(n, l, r):
    result = 0

    for a in range(l, r+1):
        b = a
        while b <= r:
            if a + b == n:
                result += 1
            b += 1

    print result
    return result

countSumOfTwoRepresentations(6, 3, 3)	# expected output 1
countSumOfTwoRepresentations(6, 2, 4)	# expected output 2
countSumOfTwoRepresentations(10, 9, 11) # expected output 0