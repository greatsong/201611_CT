n = int(input())
li = [0]*n

li[:n] = map(int, input().split())

min = max = li[0] # 가장 작은 문제를 해결
mini, maxi = 1, 1

for i in range(n) : # 작은 문제의 해결 결과 -> 큰 문제로 확장
    if li[i] > max :
        max = li[i]
        maxi = i+1
    if li[i] < min :
        min = li[i]
        mini = i+1

print(maxi,':',max)
print(mini,':',min)