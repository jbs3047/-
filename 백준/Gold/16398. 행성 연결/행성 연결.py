import heapq

n=int(input())
vis=[0 for _ in range(n)]
ans=0
lst=[[] for _ in range(n)]
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        lst[i].append([arr[i][j],j])
        lst[j].append([arr[i][j],i])
heap=[[0,0]]#가중치(0으로 초기화),시작점(아무데나)
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        for next in lst[now]:
            if not vis[next[1]]:
                heapq.heappush(heap,next)
print(ans)