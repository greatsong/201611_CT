n = int(input())
li = [0]*n

for i in range(n) :
    li[i] = int(input())

min = max = li[0]
mini, maxi = 0, 0

for i in range(n) :
    if li[i] > max :
        max = li[i]
        maxi = i+1
    if li[i] < min :
        min = li[i]
        mini = i+1

print(mini,':',min)
print(maxi,':',max)