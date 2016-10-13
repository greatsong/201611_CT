n = int(input())

cnt = 0
for a in range(1, n+1) :
    for b in range(a, n+1) :
        for c in range(b, n+1):
            if a + b + c == n and a+b > c :
                cnt += 1
print(cnt)