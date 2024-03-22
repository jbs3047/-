import heapq
INF = int(1e9)
def dijkstra(start,graph):
    q=[]
    dis=[INF for _ in range(n+1)]
    dis[start]=0
    heapq.heappush(q,(dis[start],start))
    while q:
        distance,now=heapq.heappop(q)
        if dis[now]<distance:
            continue
        for i,j in graph[now]:
            cost=distance+j
            if dis[i]>cost:
                dis[i]=cost
                heapq.heappush(q,(cost,i))
    return dis
t=int(input())
for tc in range(1,t+1):
    n,m,x=map(int,input().split())
    graph1=[[] for _ in range(n+1)]
    graph2=[[] for _ in range(n+1)]

    for _ in range(m):
        p,q,r=map(int,input().split())
        graph1[p].append((q,r))
        graph2[q].append((p,r))

    result1=dijkstra(x,graph1)
    result2=dijkstra(x,graph2)
    print(f'#{tc} {max([result1[i]+result2[i] for i in range(1,n+1)])}')