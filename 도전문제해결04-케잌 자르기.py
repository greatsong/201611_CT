a,b = map(int, input().split())
c,d = map(int, input().split())
cnt = 0

if a > b :
    a, b = b, a

for i in range(a, b+1) :
    if i == c or i == d :
        cnt+=1

if cnt== 1 :
    print('cross')
else :
    print('not cross')