def isSorted(arr):
    l = len(arr)
    if l == 0 or l == 1:
        return True
    if arr[0] > arr[1]:
        return False
    return isSorted(arr[1:])

arr = [1,2,3,4,8,6]
print(isSorted(arr))
