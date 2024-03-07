#4386 별자리 만들기
import heapq
n=int(input())
star=[list(map(float,input().split())) for _ in range(n)]
vis=[0 for _ in range(n)]
ans=0
lst=[[] for _ in range(n)]
for i in range(n-1):
    a,b=star[i]
    for j in range(i+1,n):
        c,d=star[j]
        x=((c-a)**2+(d-b)**2)**0.5
        lst[i].append([x,j])
        lst[j].append([x,i])
heap=[[0,0]]
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        for next in lst[now]:
            heapq.heappush(heap,next)
print(ans)