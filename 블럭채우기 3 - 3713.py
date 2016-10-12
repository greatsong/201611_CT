import sys
sys.setrecursionlimit(100000)

memo = [0]*10000
def f(n):
    if memo[n]:
        return memo[n]
    elif n == 1 :
        return 1
    elif n == 2 :
        return 3
    else :
        result = (f(n-1) + f(n-2)*2) % 100007
        memo[n] = result
        return result

i = int(input())

print(f(i))