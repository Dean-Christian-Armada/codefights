def kthDigit(n, k):
    x = str(n)
    if k:
        k = k-1
    if k > len(x):
        print -1
        return -1
    
    x = int(x[k])
    return x

kthDigit(578943, 10)