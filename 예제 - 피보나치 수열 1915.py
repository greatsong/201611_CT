import sys
sys.setrecursionlimit(100000)

memo = {1: 1, 2: 1}

def f(n):
    if n in memo :
        return memo[n]
    else :
        result = f(n-1) + f(n-2)
        memo[n] = result
        return result 

i = int(input())

print(f(i))