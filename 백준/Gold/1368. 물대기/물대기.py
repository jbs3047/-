import heapq

n=int(input())
water=[int(input()) for _ in range(n)]
vis=[0 for _ in range(n+1)]
ans=0
lst=[[] for _ in range(n+1)]
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        lst[i].append([arr[i][j],j])
        lst[j].append([arr[i][j],i])
for i in range(n):
    lst[n].append([water[i],i])
    lst[i].append([water[i],n])
heap=[[0,0]]
while heap:
    w,now=heapq.heappop(heap)
    if not vis[now]:
        vis[now]=1
        ans+=w
        for next in lst[now]:
            if not vis[next[1]]:
                heapq.heappush(heap,next)
print(ans)

#기본 스패닝트리 + 우물파기
#연결 or 우물값 넣기엔 문제가있음
#우물과 최소 한개는 연결되어있어야함 -> 우물이라는 노드를 추가로 생성해서 각 노드와 연결하면 될듯