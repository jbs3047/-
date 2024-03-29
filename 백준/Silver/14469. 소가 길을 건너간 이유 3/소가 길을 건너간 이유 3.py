#14469 소가 길을 건너간 이유 3
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:(x[0],x[1]))
cnt=lst[0][0]
for i in lst:
    start,time=i
    if cnt<start:
        cnt=start
    cnt+=time
print(cnt)
