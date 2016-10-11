n = int(input())

cnt = 0
for a in range(1, int(n/3)+1) :
    for b in range(a, int((n-a)/2)+1) :
        c = n - a - b
        print(a,b,c)
        if c > 0 and a+b > c :
            cnt+=1
            print(cnt,'!')
print(cnt)