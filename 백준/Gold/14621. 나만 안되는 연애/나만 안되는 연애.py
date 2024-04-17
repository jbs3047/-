import heapq

v,e=map(int,input().split())
gender=[0]+list(map(str,input().split()))
vis=[0 for _ in range(v+1)]
ans=0
lst=[[] for _ in range(v+1)]
cnt=0
for _ in range(e):
    a,b,c=map(int,input().split())
    if gender[a]==gender[b]:
        continue
    lst[a].append([c,b])
    lst[b].append([c,a])
heap=[[0,1]]
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
    print(ans)
else:
    print(-1)