def leastSignificantBit(n):

    ans = 1
    while ((n & 1) == 0):
        n >>= 1
        ans <<= 1

    print ans
    return ans


leastSignificantBit(12)