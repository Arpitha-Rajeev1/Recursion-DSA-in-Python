def count(n):
    if n == 0:
        return 1
    if n % 10 == 0:
        return 1 + count(n // 10)
    if n // 10 == 0:
        return 0
    return count(n // 10)


n = int(input())
print(count(n))
