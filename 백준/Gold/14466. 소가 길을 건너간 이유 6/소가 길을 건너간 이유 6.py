from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(y,x):
    q=deque()
    q.append((y,x))
    vis[y][x]=1
    while q:
        y,x=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=0 or nx>n or ny<=0 or ny>n:
                continue
            if [ny,nx] in lst[y][x]:
                continue
            if vis[ny][nx]:
                continue
            q.append((ny,nx))
            vis[ny][nx]=1
n,k,r=map(int,input().split())
lst=[[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    r1,c1,r2,c2=map(int,input().split())
    lst[r1][c1].append([r2,c2])
    lst[r2][c2].append([r1,c1])
cow=[list(map(int,input().split())) for _ in range(k)]
vis=[[0]*(n+1) for _ in range(n+1)]
cnt=0
for i in range(k):
    vis = [[0] * (n + 1) for _ in range(n + 1)]
    y=cow[i][0]
    x=cow[i][1]
    if vis[y][x]:
        continue
    bfs(y,x)
    for j in cow[i+1:]:
        if not vis[j[0]][j[1]]:
            cnt+=1
print(cnt)