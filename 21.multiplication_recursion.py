def product(m,n):
    print(1)
    if n == 0:
        return 0
    if m > n:
        p = m
        q = n - 1
    else:
        p = n
        q = m - 1

    return p + product(p, q)

n = int(input())
m = int(input())

print(product(m, n))
