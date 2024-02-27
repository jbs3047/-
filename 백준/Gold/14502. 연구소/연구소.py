#14502 연구소
from itertools import combinations
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
    vis=[[0 for _ in range(m)] for _ in range(n)]
    chk=0
    q=deque(virus)
    while q:
        x,y=q.popleft()
        if vis[y][x]==0:
            vis[y][x]=2
            chk+=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if lst[ny][nx]==0 and vis[ny][nx]==0:
                        q.append((nx,ny))
    return chk
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
virus=[]
empty=[]
for i in range(n):
    for j in range(m):
        if lst[i][j]==2:
            virus.append((j,i))
        elif lst[i][j]==0:
            empty.append((j,i))
cnt=len(empty)+len(virus)
ans=0

for i in combinations(empty,3):
    for x,y in i:
        lst[y][x]=1
    bfs()
    ans=max(ans,cnt-3-bfs())
    for x,y in i:
        lst[y][x]=0
print(ans)