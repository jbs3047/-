from collections import deque
def bfs(x,y):
    q=deque()
    q.append((0,y,x,1,0))
    while q:
        boom,y,x,cnt,day=q.popleft()
        if x==m-1 and y==n-1:
            return cnt
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if lst[ny][nx]==1 and boom<k and not vis[boom+1][ny][nx]:
                    if day==0:
                        vis[boom+1][ny][nx]=1
                        q.append((boom+1,ny,nx,cnt+1,day+1))
                    else:
                        vis[boom][y][x]=1
                        q.append((boom,y,x,cnt+1,(day+1)%2))
                elif lst[ny][nx]==0 and not vis[boom][ny][nx]:
                    vis[boom][ny][nx]=1
                    q.append((boom,ny,nx,cnt+1,(day+1)%2))
    return -1


dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m,k=map(int,input().split())
lst=[list(map(int,input())) for _ in range(n)]
vis=[[[0]*(m) for _ in range(n)] for _ in range(k+1)]
ans=bfs(0,0)
print(ans)
