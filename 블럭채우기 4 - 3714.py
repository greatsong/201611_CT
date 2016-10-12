import sys
sys.setrecursionlimit(1000000)

memo = [0]*100000

def f(n):
    if memo[n]:
        return memo[n]
    elif n == 1 :
        return 1
    elif n == 2 :
        return 5
    elif n == 3 :
        return 11
    else:
        result = (f(n-1)+f(n-2)*4+f(n-3)*2) % 100007
        memo[n] = result
        return result

i = int(input())

print(f(i))