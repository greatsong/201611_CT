import sys
sys.setrecursionlimit(100000)

memo = {1: 2, 2: 7, 3: 22}

def f(n):
    if n in memo:
        return memo[n]
    else:
        result = (f(n - 1) * 3 + f(n - 2) - f(n - 3))
        memo[n] = result
        return result

i = int(input())

print(f(i)% 100007)