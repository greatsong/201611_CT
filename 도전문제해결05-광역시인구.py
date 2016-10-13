import math

class myclass :
    x = 0
    y = 0
    m = 0

n, p = map(int, input().split())
li = []

def possible(m) :
    po = p
    for i in range(n) :
        if pow(li[i].x,2)+pow(li[i].y,2) <= m :
            po += li[i].m
    return po >= 1000000

for i in range(n) :
    a = myclass()
    a.x, a.y, a.m = map(int, input().split())
    li.append(a)

s = 0
e = 20001*20001

while(s < e) :
    m = (s+e-1)//2
    if possible(m) :
        e = m
    else :
        s = m + 1

if e == 20001*20001 :
    print("-1")
else :
    print("%.3f" % math.sqrt(e))