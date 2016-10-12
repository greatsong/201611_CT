import sys
sys.setrecursionlimit(100000)

memo = [0]*100000

def f(n):
    if memo[n]:
        return memo[n]
    elif n == 1 :
        return 1
    elif n == 2 :
        return 2
    elif n == 3 :
        return 6
    else:
        result = (f(n-1)+f(n-2)+f(n-3)*3) % 1000
        memo[n] = result
        return result

i = int(input())

print(f(i))