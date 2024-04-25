#14502 연구소
from itertools import combinations
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(arr):
    vis=[[0 for _ in range(n)] for _ in range(n)]
    chk=0
    q=deque(arr)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if lst[ny][nx]==0 and vis[ny][nx]==0:
                    vis[ny][nx]=vis[y][x]+1
                    q.append((nx,ny))
    for i in range(n):
        for j in range(n):
            if lst[i][j]==0 and vis[i][j]==0:
                return -1
            chk=max(chk,vis[i][j])
    return chk
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
virus=[]
empty=[]
for i in range(n):
    for j in range(n):
        if lst[i][j]==2:
            virus.append((j,i))
            lst[i][j]=0
        elif lst[i][j]==0:
            empty.append((j,i))
ans=-1
for i in combinations(virus,m):
    for x,y in i:
        lst[y][x]=2
    if ans==-1:
        if bfs(i)!=-1:
            ans=bfs(i)
    else:
        if bfs(i)!=-1:
            ans=min(ans,bfs(i))
    for x,y in i:
        lst[y][x]=0
print(ans)