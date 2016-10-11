import sys
sys.setrecursionlimit(100000)

memo = {0:0, 1: 1, 2: 2, 3: 6}

def f(n):
    if n in memo:
        return memo[n]
    else:
        result = (f(n-1)+f(n-2)+f(n-3)*3) % 1000
        memo[n] = result
        return result

i = int(input())

print(f(i))