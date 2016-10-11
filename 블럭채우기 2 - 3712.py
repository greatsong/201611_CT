import sys
sys.setrecursionlimit(100000)

memo = {3: 2}

def f(n):
    if n <= 2 :
        return 0
    if n in memo :
        return memo[n]
    else :
        result = (2 * f(n-3)) % 100000007
        memo[n] = result
        return result

i = int(input())

print(f(i))