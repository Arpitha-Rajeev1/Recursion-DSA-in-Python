def merge(arr1, arr2, arr):
    a1 = len(arr1)
    a2 = len(arr2)
    i = 0
    j = 0
    k = 0
    while i < a1 and j < a2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < a1:
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1
    while j < a2:
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1

def mergeSort(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    mid = n // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    
    mergeSort(arr1)
    mergeSort(arr2)
    
    merge(arr1, arr2, arr)

# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
 
