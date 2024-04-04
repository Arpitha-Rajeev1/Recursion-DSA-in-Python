def finding(arr, x, si, result):
    if len(arr) == 0:
        return result
    if x == arr[0]:
        result.append(si)
        return finding(arr[1:], x, si + 1, result)
    return finding(arr[1:], x, si + 1, result)

x = int(input())
arr = list(int(i) for i in input().strip().split(' '))
result = []
print(finding(arr, x, 0, result))
