dx=[-1,1,0,0]
dy=[0,0,-1,1]
import heapq

def dijkstra(n):
    q=[]
    heapq.heappush(q,[lst[0][0],0,0])
    while q:
        cnt,x,y=heapq.heappop(q)
        if x==n-1 and y==n-1:
            ans=cnt
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and lst[ny][nx]!=-1:
                heapq.heappush(q,(cnt+lst[ny][nx],nx,ny))
                lst[ny][nx]=-1
    return ans


cnt=1
while True:
    INF=1e9
    n=int(input())
    if n==0:
        break
    lst=[list(map(int,input().split())) for _ in range(n)]
    ans=dijkstra(n)
    print(f'Problem {cnt}: {ans}')
    cnt+=1