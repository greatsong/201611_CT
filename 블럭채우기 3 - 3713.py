import sys
sys.setrecursionlimit(100000)

memo = {1: 1, 2: 3}

def f(n):
    if n in memo :
        return memo[n]
    else :
        result = (f(n-1) + f(n-2)*2) % 100007
        memo[n] = result
        return result

i = int(input())

print(f(i))