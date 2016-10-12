n = int(input())
ans = 0
for i in range(1,n+1) : # 주어진 범위를 모두 탐색한다.
    if n % i == 0 :
        ans += i
print(ans)