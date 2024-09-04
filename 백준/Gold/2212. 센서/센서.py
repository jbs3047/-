# 2212 센서
n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()

sensor = []
for i in range(n - 1):
    sensor.append(lst[i + 1] - lst[i])

sensor.sort()

ans = 0
for i in range(n - k):
    ans += sensor[i]
print(ans)
