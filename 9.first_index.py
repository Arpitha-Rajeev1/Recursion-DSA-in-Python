def firstIndex(arr, x, si):
    if len(arr) == 0:
        return -1
    if arr[0] == x:
        return si
    return firstIndex(arr[1:], x, si+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(firstIndex(arr, x, 0))
