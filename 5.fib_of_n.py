def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

import sys
sys.setrecursionlimit(3000)

n = int(input())
print(fib(n))
