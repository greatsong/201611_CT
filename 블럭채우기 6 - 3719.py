import sys
sys.setrecursionlimit(100000)

memo = [0]*10000

def f(n):
    if memo[n]:
        return memo[n]
    elif n == 1 :
        return 2
    elif n == 2 :
        return 7
    elif n == 3 :
        return 22
    else:
        result = (f(n - 1) * 3 + f(n - 2) - f(n - 3))
        memo[n] = result
        return result

i = int(input())

print(f(i)% 100007)