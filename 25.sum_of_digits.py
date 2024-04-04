def sum(n):
    if n == 0:
        return n
    remainder = n % 10
    return remainder + sum(n // 10)


n = int(input())
print(sum(n))
