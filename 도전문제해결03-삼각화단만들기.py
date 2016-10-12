n = int(input())
cnt = 0

for a in range(1, int(n/3)+1) :
    for b in range(int((n-2*a)/2), int((n-a)/2)+1) :
        c = n - a - b
        if a + b + c == n and  c > 0 :
                cnt += 1
print(cnt)