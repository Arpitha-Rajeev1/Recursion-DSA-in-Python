def partition(a, si, ei):
    pivot = a[ei]
    i = si - 1
    for j in range(si, ei+1):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    return i

def quick_sort(a,si,ei):
    if si >= ei:
        return a

    pivot_index = partition(a, si, ei)
    quick_sort(a, si, pivot_index - 1)
    quick_sort(a, pivot_index + 1, ei)

a = [10, 9, 8, 7, 1, 3, 5, 4, 2]
quick_sort(a, 0, len(a)-1)
print(a)
