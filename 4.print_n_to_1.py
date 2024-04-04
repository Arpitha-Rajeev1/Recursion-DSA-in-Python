def printn(n):
    if n == 0:
        return
    print(n)
    printn(n-1)

n = int(input())
printn(n)
