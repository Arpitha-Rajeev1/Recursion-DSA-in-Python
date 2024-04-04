def binary(arr, m):
    n = len(arr)
    if n == 1:
        return arr[0] == m
    mid = n // 2
    return arr[mid] == m
    if m > arr[mid]:
        return binary(arr[mid+1:], m)
    elif m < arr[mid]:
        return binary(arr[:mid],m)

def binarySearch(a, x, si, ei):
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a, x, si, mid - 1)
    else:
        return binarySearch(a, x, mid + 1, ei)

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
m = int(input())
print(binary(arr, m))
