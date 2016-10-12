import sys
sys.setrecursionlimit(100000)

memo = [0]*10000
def f(n):
    if memo[n]:
        return memo[n]
    elif n <= 2 :
        return 0
    elif n == 3 :
        return 2
    else :
        result = (2 * f(n-3)) % 100000007
        memo[n] = result
        return result

i = int(input())

print(f(i))