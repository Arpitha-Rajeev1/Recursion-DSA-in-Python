from sys import setrecursionlimit


def lastIndex(arr, x, si):
    if len(arr) == 0:
        return -1
    if arr[si] == x:
        return si
    return lastIndex(arr[:si], x, si-1)


# Main
setrecursionlimit(11000)

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(lastIndex(arr, x, len(arr)-1))
