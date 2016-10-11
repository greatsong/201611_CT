a, b = map(int, input().split())
gcd = 1
for i in range(2,a+1) :
    if b % i == 0 and a % i == 0:
        if i > gcd :
            gcd = i
print(gcd)