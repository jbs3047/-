from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    vis[y][x]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not vis[ny][nx] and arr[ny][nx]:
                    vis[ny][nx]=1
                    q.append((nx,ny))
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
ans=0
while True:
    bing=0
    arr=[x[:] for x in lst]
    vis = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                for k in range(4):
                    nx=j+dx[k]
                    ny=i+dy[k]
                    if 0<=nx<m and 0<=ny<n:
                        if not lst[ny][nx]:
                            arr[i][j]-=1
                            if arr[i][j]==0:
                                break
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not vis[i][j]:
                bfs(j,i)
                bing+=1
    chk=0
    ans += 1
    lst=[x[:] for x in arr]
    if bing==0:
        break
    if bing>=2:
        chk=1
        break
if chk:
    print(ans)
else:
    print(0)