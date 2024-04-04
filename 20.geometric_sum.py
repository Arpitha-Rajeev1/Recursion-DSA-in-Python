#Geometric sum: 1 + 1/(2^1) + 1/(2^2) + .... + 1/(2^k)

def gs(k):
    if k == 0:
        return 1
    return 1/(2**k) + gs(k-1)

k = int(input())
print('%.5f' % gs(k))
