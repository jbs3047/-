import heapq

v,e=map(int,input().split())
vis=[0 for _ in range(v+1)]
ans=0
lst=[[] for _ in range(v+1)]
sm=0
cnt=0
for _ in range(e):
    a,b,c=map(int,input().split())
    lst[a].append([c,b])#가중치,경로
    lst[b].append([c,a])
    sm+=c
heap=[[0,1]]#가중치(0으로 초기화),시작점(아무데나)
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        cnt+=1
        for next in lst[now]:
            if not vis[next[1]]:
                heapq.heappush(heap,next)

if cnt==v:
    print(sm-ans)
else:
    print(-1)