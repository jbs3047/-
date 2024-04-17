import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
star=[[]]+[list(map(int,input().split())) for _ in range(n)]
link=set()
for _ in range(m):
    x,y=map(int,input().split())
    link.add((x,y))
    link.add((y,x))
vis=[0 for _ in range(n+1)]
ans=0
lst=[[] for _ in range(n+1)]
for i in range(1,n):
    a,b=star[i]
    for j in range(i+1,n+1):
        c,d=star[j]
        if (i,j) in link:
            lst[i].append([0,j])
            lst[j].append([0,i])
        else:
            x=((c-a)**2+(d-b)**2)**0.5
            lst[i].append([x,j])
            lst[j].append([x,i])
heap=[[0,1]]
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        for next in lst[now]:
            if not vis[next[1]]:
                heapq.heappush(heap,next)
print("%.2f"%ans)



