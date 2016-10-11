import sys
sys.setrecursionlimit(1000000)

memo = {1: 1, 2: 5, 3: 11}

def f(n):
    if n in memo:
        return memo[n]
    else:
        result = (f(n-1)+f(n-2)*4+f(n-3)*2) % 100007
        memo[n] = result
        return result

i = int(input())

print(f(i))