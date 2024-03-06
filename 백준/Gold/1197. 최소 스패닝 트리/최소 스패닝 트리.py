import heapq

v,e=map(int,input().split())
vis=[0 for _ in range(v+1)]
ans=0
lst=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    lst[a].append([c,b])#가중치,경로
    lst[b].append([c,a])
heap=[[0,1]]#가중치(0으로 초기화),시작점(아무데나)
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        for next in lst[now]:
            heapq.heappush(heap,next)
print(ans)