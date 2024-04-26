#14464 소가 길을 건너간 이유 4
from collections import deque
c,n=map(int,input().split())
chicken=[int(input()) for _ in range(c)]
cow=[list(map(int,input().split())) for _ in range(n)]
chicken.sort()
cow.sort(key=lambda x:(x[1],x[0]))
cows=deque(cow)
cnt=0
while cows and chicken:
    cow=cows.popleft()
    for i in range(len(chicken)):
        if cow[0]<=chicken[i]<=cow[1]:
            cnt+=1
            del chicken[i]
            break
print(cnt)