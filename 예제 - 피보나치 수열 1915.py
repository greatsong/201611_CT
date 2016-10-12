import sys
sys.setrecursionlimit(100000)

memo = [0]*100000

def f(n):
    if memo[n]:
        return memo[n]
    elif n <= 2 :
        return 1
    else :
        result = f(n-1) + f(n-2)
        memo[n] = result
        return result 

i = int(input())

print(f(i))